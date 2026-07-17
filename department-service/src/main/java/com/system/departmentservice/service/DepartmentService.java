package com.system.departmentservice.service;
import com.system.departmentservice.dto.DepartmentDto;
import java.util.List;

public interface DepartmentService {
    DepartmentDto createDepartment(DepartmentDto dto);
    DepartmentDto getDepartmentById(Long id);
    List<DepartmentDto> getAllDepartments();
    DepartmentDto updateDepartment(Long id, DepartmentDto dto);
    void deleteDepartment(Long id);
}
