package com.system.notificationservice.service.impl;
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
