package com.system.notificationservice.controller;
import com.system.notificationservice.dto.NotificationDto;
import com.system.notificationservice.service.NotificationService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import lombok.RequiredArgsConstructor;
import java.util.List;

@RestController
@RequestMapping("/api/notifications")
@RequiredArgsConstructor
public class NotificationController {
    
    private final NotificationService service;

    @PostMapping
    public ResponseEntity<NotificationDto> create(@RequestBody NotificationDto dto) {
        return new ResponseEntity<>(service.createNotification(dto), HttpStatus.CREATED);
    }

    @GetMapping("/{id}")
    public ResponseEntity<NotificationDto> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getNotificationById(id));
    }

    @GetMapping
    public ResponseEntity<List<NotificationDto>> getAll() {
        return ResponseEntity.ok(service.getAllNotifications());
    }

    @PutMapping("/{id}")
    public ResponseEntity<NotificationDto> update(@PathVariable Long id, @RequestBody NotificationDto dto) {
        return ResponseEntity.ok(service.updateNotification(id, dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        service.deleteNotification(id);
        return ResponseEntity.noContent().build();
    }
}
