package com.system.leaveservice.service;
import com.system.leaveservice.dto.LeaveDto;
import java.util.List;

public interface LeaveService {
    LeaveDto createLeave(LeaveDto dto);
    LeaveDto getLeaveById(Long id);
    List<LeaveDto> getAllLeaves();
    LeaveDto updateLeave(Long id, LeaveDto dto);
    void deleteLeave(Long id);
}
