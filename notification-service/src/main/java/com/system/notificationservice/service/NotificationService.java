package com.system.notificationservice.service;
import com.system.notificationservice.dto.NotificationDto;
import java.util.List;

public interface NotificationService {
    NotificationDto createNotification(NotificationDto dto);
    NotificationDto getNotificationById(Long id);
    List<NotificationDto> getAllNotifications();
    NotificationDto updateNotification(Long id, NotificationDto dto);
    void deleteNotification(Long id);
}
