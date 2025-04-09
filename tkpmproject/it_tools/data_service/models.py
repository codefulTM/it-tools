from django.db import models

# Create your models here.
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(50) UNIQUE NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     password_hash TEXT NOT NULL,
#     role_id INT REFERENCES user_roles(id) ON DELETE CASCADE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.CharField(max_length=100, unique=True, null=False)
    password_hash = models.TextField(null=False)
    role_id = models.ForeignKey('UserRole', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# CREATE TABLE user_roles (
#   id SERIAL PRIMARY KEY,
#   role VARCHAR(20) UNIQUE NOT NULL
# );
class UserRole(models.Model):
    id = models.AutoField(primary_key=True) 
    role = models.CharField(max_length=20, unique=True, null=False)

# CREATE TABLE tools (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) UNIQUE NOT NULL,
#     description TEXT,
#     category_id INT REFERENCES tool_categories(id) ON DELETE CASCADE,
#     is_premium BOOLEAN DEFAULT FALSE,
#     is_enabled BOOLEAN DEFAULT TRUE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=True)
    category_id = models.ForeignKey('ToolCategory', on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

# CREATE TABLE tool_categories(
#   id SERIAL PRIMARY KEY,
#   name TEXT UNIQUE NOT NULL
# );
class ToolCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True, null=False)

# CREATE TABLE favorites (
#     id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES users(id) ON DELETE CASCADE,
#     tool_id INT REFERENCES tools(id) ON DELETE CASCADE,
#     UNIQUE(user_id, tool_id)
# );
class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    tool_id = models.ForeignKey('Tool', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user_id', 'tool_id')

# CREATE TABLE subscriptions (
#     id SERIAL PRIMARY KEY,
#     user_id INT REFERENCES users(id) ON DELETE CASCADE,
#     status_id INT REFERENCES subscription_statuses(id) ON DELETE CASCADE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    status_id = models.ForeignKey('SubscriptionStatus', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

# CREATE TABLE subscription_statuses (
#   id SERIAL PRIMARY KEY,
#   status_name TEXT UNIQUE NOT NULL
# );
class SubscriptionStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_name = models.TextField(unique=True, null=False)

# CREATE TABLE system_parameters (
#   id SERIAL PRIMARY KEY,
#   param_key VARCHAR(100) UNIQUE NOT NULL,
#   param_value TEXT NOT NULL,
#   description TEXT
# );
class SystemParameter(models.Model):
    id = models.AutoField(primary_key=True)
    param_key = models.CharField(max_length=100, unique=True, null=False)
    param_value = models.TextField(null=False)
    description = models.TextField(null=True)