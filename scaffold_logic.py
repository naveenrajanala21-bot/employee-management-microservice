import os

base_dir = r"c:\Users\ADMIN\Desktop\projects\employee-management-microservice"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_entity(package, entity_class, fields=""):
    return f"""package {package}.entity;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "{entity_class.lower()}s")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class {entity_class} {{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    {fields}
}}
"""

def generate_repo(package, entity_class):
    return f"""package {package}.repository;
import {package}.entity.{entity_class};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {entity_class}Repository extends JpaRepository<{entity_class}, Long> {{
}}
"""

def generate_dto(package, entity_class, fields=""):
    return f"""package {package}.dto;
import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class {entity_class}Dto {{
    private Long id;
    {fields}
}}
"""

def generate_service(package, entity_class):
    return f"""package {package}.service;
import {package}.dto.{entity_class}Dto;
import java.util.List;

public interface {entity_class}Service {{
    {entity_class}Dto create{entity_class}({entity_class}Dto dto);
    {entity_class}Dto get{entity_class}ById(Long id);
    List<{entity_class}Dto> getAll{entity_class}s();
    {entity_class}Dto update{entity_class}(Long id, {entity_class}Dto dto);
    void delete{entity_class}(Long id);
}}
"""

def generate_service_impl(package, entity_class):
    return f"""package {package}.service.impl;
import {package}.dto.{entity_class}Dto;
import {package}.entity.{entity_class};
import {package}.repository.{entity_class}Repository;
import {package}.service.{entity_class}Service;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class {entity_class}ServiceImpl implements {entity_class}Service {{
    
    private final {entity_class}Repository repository;

    @Override
    public {entity_class}Dto create{entity_class}({entity_class}Dto dto) {{
        {entity_class} entity = new {entity_class}();
        // manual map
        entity = repository.save(entity);
        dto.setId(entity.getId());
        return dto;
    }}

    @Override
    public {entity_class}Dto get{entity_class}ById(Long id) {{
        return repository.findById(id).map(e -> {{
            {entity_class}Dto dto = new {entity_class}Dto();
            dto.setId(e.getId());
            return dto;
        }}).orElseThrow(() -> new RuntimeException("{entity_class} not found"));
    }}

    @Override
    public List<{entity_class}Dto> getAll{entity_class}s() {{
        return repository.findAll().stream().map(e -> {{
            {entity_class}Dto dto = new {entity_class}Dto();
            dto.setId(e.getId());
            return dto;
        }}).collect(Collectors.toList());
    }}

    @Override
    public {entity_class}Dto update{entity_class}(Long id, {entity_class}Dto dto) {{
        {entity_class} entity = repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return dto;
    }}

    @Override
    public void delete{entity_class}(Long id) {{
        repository.deleteById(id);
    }}
}}
"""

def generate_controller(package, entity_class):
    return f"""package {package}.controller;
import {package}.dto.{entity_class}Dto;
import {package}.service.{entity_class}Service;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import lombok.RequiredArgsConstructor;
import java.util.List;

@RestController
@RequestMapping("/api/{entity_class.lower()}s")
@RequiredArgsConstructor
public class {entity_class}Controller {{
    
    private final {entity_class}Service service;

    @PostMapping
    public ResponseEntity<{entity_class}Dto> create(@RequestBody {entity_class}Dto dto) {{
        return new ResponseEntity<>(service.create{entity_class}(dto), HttpStatus.CREATED);
    }}

    @GetMapping("/{{id}}")
    public ResponseEntity<{entity_class}Dto> getById(@PathVariable Long id) {{
        return ResponseEntity.ok(service.get{entity_class}ById(id));
    }}

    @GetMapping
    public ResponseEntity<List<{entity_class}Dto>> getAll() {{
        return ResponseEntity.ok(service.getAll{entity_class}s());
    }}

    @PutMapping("/{{id}}")
    public ResponseEntity<{entity_class}Dto> update(@PathVariable Long id, @RequestBody {entity_class}Dto dto) {{
        return ResponseEntity.ok(service.update{entity_class}(id, dto));
    }}

    @DeleteMapping("/{{id}}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {{
        service.delete{entity_class}(id);
        return ResponseEntity.noContent().build();
    }}
}}
"""

def generate_exception(package):
    return f"""package {package}.exception;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {{
    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleException(Exception ex) {{
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }}
}}
"""

services = [("employee", "Employee"), ("department", "Department"), ("leave", "Leave"), ("notification", "Notification")]
for s, ec in services:
    name = f"{s}-service"
    package = f"com.system.{s}service"
    base = f"{name}/src/main/java/{package.replace('.','/')}"
    
    write_file(f"{base}/entity/{ec}.java", generate_entity(package, ec, "private String name;"))
    write_file(f"{base}/repository/{ec}Repository.java", generate_repo(package, ec))
    write_file(f"{base}/dto/{ec}Dto.java", generate_dto(package, ec, "private String name;"))
    write_file(f"{base}/service/{ec}Service.java", generate_service(package, ec))
    write_file(f"{base}/service/impl/{ec}ServiceImpl.java", generate_service_impl(package, ec))
    write_file(f"{base}/controller/{ec}Controller.java", generate_controller(package, ec))
    write_file(f"{base}/exception/GlobalExceptionHandler.java", generate_exception(package))

# Modify Notification to not have a controller for REST but rather a mock email send
mock_notification = """package com.system.notificationservice.service.impl;
import com.system.notificationservice.dto.NotificationDto;
import com.system.notificationservice.entity.Notification;
import com.system.notificationservice.repository.NotificationRepository;
import com.system.notificationservice.service.NotificationService;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;
import java.util.List;
import lombok.extern.slf4j.Slf4j;

@Service
@RequiredArgsConstructor
@Slf4j
public class NotificationServiceImpl implements NotificationService {
    private final NotificationRepository repository;

    @Override
    public NotificationDto createNotification(NotificationDto dto) {
        log.info("Sending mock email to: " + dto.getName());
        return dto;
    }
    @Override public NotificationDto getNotificationById(Long id) { return null; }
    @Override public List<NotificationDto> getAllNotifications() { return null; }
    @Override public NotificationDto updateNotification(Long id, NotificationDto dto) { return null; }
    @Override public void deleteNotification(Long id) { }
}
"""
write_file("notification-service/src/main/java/com/system/notificationservice/service/impl/NotificationServiceImpl.java", mock_notification)

print("Logic scaffolding done.")
