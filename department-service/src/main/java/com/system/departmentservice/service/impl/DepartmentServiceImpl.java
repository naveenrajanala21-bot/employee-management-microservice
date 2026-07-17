package com.system.departmentservice.service.impl;
import com.system.departmentservice.dto.DepartmentDto;
import com.system.departmentservice.entity.Department;
import com.system.departmentservice.repository.DepartmentRepository;
import com.system.departmentservice.service.DepartmentService;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class DepartmentServiceImpl implements DepartmentService {
    
    private final DepartmentRepository repository;

    @Override
    public DepartmentDto createDepartment(DepartmentDto dto) {
        Department entity = new Department();
        // manual map
        entity = repository.save(entity);
        dto.setId(entity.getId());
        return dto;
    }

    @Override
    public DepartmentDto getDepartmentById(Long id) {
        return repository.findById(id).map(e -> {
            DepartmentDto dto = new DepartmentDto();
            dto.setId(e.getId());
            return dto;
        }).orElseThrow(() -> new RuntimeException("Department not found"));
    }

    @Override
    public List<DepartmentDto> getAllDepartments() {
        return repository.findAll().stream().map(e -> {
            DepartmentDto dto = new DepartmentDto();
            dto.setId(e.getId());
            return dto;
        }).collect(Collectors.toList());
    }

    @Override
    public DepartmentDto updateDepartment(Long id, DepartmentDto dto) {
        Department entity = repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return dto;
    }

    @Override
    public void deleteDepartment(Long id) {
        repository.deleteById(id);
    }
}
