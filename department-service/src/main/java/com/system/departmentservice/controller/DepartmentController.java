package com.system.departmentservice.controller;
import com.system.departmentservice.dto.DepartmentDto;
import com.system.departmentservice.service.DepartmentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import lombok.RequiredArgsConstructor;
import java.util.List;

@RestController
@RequestMapping("/api/departments")
@RequiredArgsConstructor
public class DepartmentController {
    
    private final DepartmentService service;

    @PostMapping
    public ResponseEntity<DepartmentDto> create(@RequestBody DepartmentDto dto) {
        return new ResponseEntity<>(service.createDepartment(dto), HttpStatus.CREATED);
    }

    @GetMapping("/{id}")
    public ResponseEntity<DepartmentDto> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getDepartmentById(id));
    }

    @GetMapping
    public ResponseEntity<List<DepartmentDto>> getAll() {
        return ResponseEntity.ok(service.getAllDepartments());
    }

    @PutMapping("/{id}")
    public ResponseEntity<DepartmentDto> update(@PathVariable Long id, @RequestBody DepartmentDto dto) {
        return ResponseEntity.ok(service.updateDepartment(id, dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        service.deleteDepartment(id);
        return ResponseEntity.noContent().build();
    }
}
