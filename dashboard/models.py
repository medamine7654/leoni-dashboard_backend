
from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    operating_system = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100, null=True, blank=True)
    mac_address = models.CharField(max_length=50, null=True, blank=True)
    model_id = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class UserVerification(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='verifications')
    last_login_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    has_admin_rights = models.BooleanField(default=False)
    password_never_expires = models.BooleanField(default=False)
    verified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Verification for {self.computer.name}"

class VPNStatus(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='vpn_status')
    username = models.CharField(max_length=100)
    is_connected = models.BooleanField(default=False)
    last_connection = models.DateTimeField(null=True, blank=True)
    verified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"VPN Status for {self.username} on {self.computer.name}"

class VerificationTask(models.Model):
    TASK_TYPES = (
        ('user_verification', 'User Verification'),
        ('admin_rights', 'Admin Rights Check'),
        ('vpn_status', 'VPN Status Check'),
        ('password_expiry', 'Password Expiry Check'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    computers = models.ManyToManyField(Computer, blank=True, related_name='verification_tasks')
    scheduled_time = models.DateTimeField()
    execution_time = models.DateTimeField(null=True, blank=True)
    result_summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.task_type} - {self.status}"