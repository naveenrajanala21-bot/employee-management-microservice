package com.system.leaveservice.controller;
import com.system.leaveservice.dto.LeaveDto;
import com.system.leaveservice.service.LeaveService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import lombok.RequiredArgsConstructor;
import java.util.List;

@RestController
@RequestMapping("/api/leaves")
@RequiredArgsConstructor
public class LeaveController {
    
    private final LeaveService service;

    @PostMapping
    public ResponseEntity<LeaveDto> create(@RequestBody LeaveDto dto) {
        return new ResponseEntity<>(service.createLeave(dto), HttpStatus.CREATED);
    }

    @GetMapping("/{id}")
    public ResponseEntity<LeaveDto> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getLeaveById(id));
    }

    @GetMapping
    public ResponseEntity<List<LeaveDto>> getAll() {
        return ResponseEntity.ok(service.getAllLeaves());
    }

    @PutMapping("/{id}")
    public ResponseEntity<LeaveDto> update(@PathVariable Long id, @RequestBody LeaveDto dto) {
        return ResponseEntity.ok(service.updateLeave(id, dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        service.deleteLeave(id);
        return ResponseEntity.noContent().build();
    }
}
