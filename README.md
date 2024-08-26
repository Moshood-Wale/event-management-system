# Event Management System

## Overview

This is a simple event management system built with Django and Django REST Framework. It allows users to create events, view tickets, and buy tickets. This system is ideal for managing event-related data and ticket sales.

## Features

- **Create and Manage Events**: Add new events with details such as name, description, date, and location.
- **View Tickets**: List all available tickets for events.
- **Buy Tickets**: Purchase tickets for an event, ensuring that the number of available tickets is updated.

## Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. **Clone the Repository**

    git clone https://github.com/Moshood-Wale/event-management-system.git
    cd bookings

2. **Create and Activate a Virtual Environment**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

    pip install -r requirements.txt

4. **Apply Migrations**

    python manage.py makemigrations
    python manage.py migrate

5. **Run the Development Server**

    python manage.py runserver

### API Endpoints

- **Create an Event**
  - `POST /api/events/`
  - Request Body:
    ```json
    {
      "name": "Concert",
      "description": "Live music concert",
      "date": "2024-09-01T20:00:00Z",
      "location": "City Stadium"
    }
    ```

- **Create a Ticket**
  - `POST /api/tickets/`
  - Request Body:
    ```json
    {
      "event": 1,
      "ticket_type": "VIP",
      "price": 100.00,
      "quantity": 50
    }
    ```

- **View Tickets**
  - `GET /api/tickets/`

- **Buy a Ticket**
  - `POST /api/tickets/<id>/buy/`
  - Request Body:
    ```json
    {
      "quantity": 2
    }
    ```