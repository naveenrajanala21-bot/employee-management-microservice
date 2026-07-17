package com.system.employeeservice.service.impl;
import com.system.employeeservice.dto.EmployeeDto;
import com.system.employeeservice.entity.Employee;
import com.system.employeeservice.repository.EmployeeRepository;
import com.system.employeeservice.service.EmployeeService;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class EmployeeServiceImpl implements EmployeeService {
    
    private final EmployeeRepository repository;

    @Override
    public EmployeeDto createEmployee(EmployeeDto dto) {
        Employee entity = new Employee();
        // manual map
        entity = repository.save(entity);
        dto.setId(entity.getId());
        return dto;
    }

    @Override
    public EmployeeDto getEmployeeById(Long id) {
        return repository.findById(id).map(e -> {
            EmployeeDto dto = new EmployeeDto();
            dto.setId(e.getId());
            return dto;
        }).orElseThrow(() -> new RuntimeException("Employee not found"));
    }

    @Override
    public List<EmployeeDto> getAllEmployees() {
        return repository.findAll().stream().map(e -> {
            EmployeeDto dto = new EmployeeDto();
            dto.setId(e.getId());
            return dto;
        }).collect(Collectors.toList());
    }

    @Override
    public EmployeeDto updateEmployee(Long id, EmployeeDto dto) {
        Employee entity = repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return dto;
    }

    @Override
    public void deleteEmployee(Long id) {
        repository.deleteById(id);
    }
}
