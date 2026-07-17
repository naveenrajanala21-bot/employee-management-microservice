package com.system.leaveservice.service.impl;
import com.system.leaveservice.dto.LeaveDto;
import com.system.leaveservice.entity.Leave;
import com.system.leaveservice.repository.LeaveRepository;
import com.system.leaveservice.service.LeaveService;
import org.springframework.stereotype.Service;
import lombok.RequiredArgsConstructor;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class LeaveServiceImpl implements LeaveService {
    
    private final LeaveRepository repository;

    @Override
    public LeaveDto createLeave(LeaveDto dto) {
        Leave entity = new Leave();
        // manual map
        entity = repository.save(entity);
        dto.setId(entity.getId());
        return dto;
    }

    @Override
    public LeaveDto getLeaveById(Long id) {
        return repository.findById(id).map(e -> {
            LeaveDto dto = new LeaveDto();
            dto.setId(e.getId());
            return dto;
        }).orElseThrow(() -> new RuntimeException("Leave not found"));
    }

    @Override
    public List<LeaveDto> getAllLeaves() {
        return repository.findAll().stream().map(e -> {
            LeaveDto dto = new LeaveDto();
            dto.setId(e.getId());
            return dto;
        }).collect(Collectors.toList());
    }

    @Override
    public LeaveDto updateLeave(Long id, LeaveDto dto) {
        Leave entity = repository.findById(id).orElseThrow(() -> new RuntimeException("Not found"));
        return dto;
    }

    @Override
    public void deleteLeave(Long id) {
        repository.deleteById(id);
    }
}
