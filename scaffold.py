import os

base_dir = r"c:\Users\ADMIN\Desktop\projects\employee-management-microservice"

# Modules configuration
modules = [
    "eureka-server",
    "config-server",
    "api-gateway",
    "employee-service",
    "department-service",
    "leave-service",
    "notification-service"
]

project_structure = {
    "pom.xml": """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.system</groupId>
    <artifactId>employee-management</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    
    <modules>
""" + "".join([f"        <module>{m}</module>\n" for m in modules]) + """    </modules>

    <properties>
        <java.version>21</java.version>
        <spring-boot.version>3.2.4</spring-boot.version>
        <spring-cloud.version>2023.0.1</spring-cloud.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
""",
    "docker-compose.yml": """version: '3.8'
services:
  eureka-server:
    build: ./eureka-server
    ports:
      - "8761:8761"
    environment:
      - EUREKA_CLIENT_REGISTERWITHEUREKA=false
      - EUREKA_CLIENT_FETCHREGISTRY=false
""",
}

for module in modules:
    package_path = f"{module}/src/main/java/com/system/{module.replace('-', '')}"
    resource_path = f"{module}/src/main/resources"
    test_path = f"{module}/src/test/java/com/system/{module.replace('-', '')}"

    os.makedirs(os.path.join(base_dir, package_path), exist_ok=True)
    os.makedirs(os.path.join(base_dir, resource_path), exist_ok=True)
    os.makedirs(os.path.join(base_dir, test_path), exist_ok=True)
    
    # Generic module POM
    project_structure[f"{module}/pom.xml"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.system</groupId>
        <artifactId>employee-management</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
    <artifactId>{module}</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
"""
    project_structure[f"{module}/Dockerfile"] = """FROM eclipse-temurin:21-jdk-alpine
VOLUME /tmp
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
"""
    project_structure[f"{module}/src/main/resources/application.yml"] = f"""server:
  port: 8080
spring:
  application:
    name: {module}
"""

def write_files(items, current_dir):
    for name, content in items.items():
        path = os.path.join(current_dir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

write_files(project_structure, base_dir)
print("Scaffolding complete.")
