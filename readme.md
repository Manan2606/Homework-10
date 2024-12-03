# Event Manager

## Overview

Event Manager is a Python-based application built using FastAPI that allows users to manage their profiles, including email verification, password management, and social media integration. This project integrates with PostgreSQL and utilizes JWT tokens for authentication. It also includes automated testing with Pytest.

## Features

- **User Registration & Authentication**
  - Users can register and authenticate via JWT tokens.
  - Roles such as ADMIN and MANAGER are supported with role-based access control.

- **Email Verification**
  - Users must verify their email to complete registration.
  - Email verification is managed using external email services like Mailtrap for testing.

- **Profile Management**
  - Users can set and update their profile information, including nickname, profile picture URL, and social media URLs.

- **Password Validation**
  - Strong password validation is enforced during registration and profile update.

- **Unique Username Validation**
  - The application ensures that all usernames (nicknames) are unique.

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- PostgreSQL
- Docker (for containerized setup)

### Issues Solved

## Issues Solved

### 1. [JWT Token and Pytest Error](https://github.com/Manan2606/Homework-10/issues/1)
   - **Problem**: Login Authentication failed for users with ADMIN, MANAGER roles due to JWT token issues.
   - **Solution**: Fixed JWT token generation and authentication logic to correctly handle user roles during login.
   - **Pytest Errors**: Addressed various Pytest issues to ensure smooth testing of authentication and email verification.

### 2. [Nickname Mismatched in Register](https://github.com/Manan2606/Homework-10/issues/2)
   - **Problem**: There was a mismatch in the nickname provided during user registration.
   - **Solution**: Corrected the logic to ensure consistent nickname handling across the registration process.

### 3. [Password Validation](https://github.com/Manan2606/Homework-10/issues/4)
   - **Problem**: The application lacked proper password validation.
   - **Solution**: Implemented password strength validation to ensure security and user compliance.

### 4. [Unique Username (Nickname) Validation](https://github.com/Manan2606/Homework-10/issues/6)
   - **Problem**: Users could insert the same nickname, which was invalid.
   - **Solution**: Added unique nickname validation to prevent duplicate usernames during registration.

### 5. [URL Validation](https://github.com/Manan2606/Homework-10/issues/8)
   - **Problem**: Invalid URLs could be provided in fields such as `profile_picture_url`, `linkedin_profile_url`, and `github_profile_url`.
   - **Solution**: Implemented URL validation to ensure that all URLs provided are valid and correctly formatted.

### 6. [Unverified Email Users](https://github.com/Manan2606/Homework-10/issues/10)
   - **Problem**: Users with unverified emails could update their profiles, leading to potential security issues.
   - **Solution**: Added a check to ensure that only verified email users can update their profile information.



### Outcomes
The project demonstrates how to manage user profiles with JWT authentication and validation.
Implemented various checks and balances to ensure data integrity, security, and compliance with best practices.
Successfully set up continuous integration and testing with Pytest, ensuring robustness and reliability.
