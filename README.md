# Event Management System (EMS)

<mark>NOTE: This project is not complete.</mark>

## Setup and Installation

Follow these steps to set up and run the **Event Management System (EMS)** project on your local machine:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd ems
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database
Ensure you have PostgreSQL installed and running. Create a database for the project.

```sql
CREATE DATABASE ems;
```

Update `ems/settings.py` with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ems',  # Database name
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompt to create an admin account.

### 7. Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## About EMS - Event Management System

EMS is a powerful event planning and management system that streamlines event organization, service selection, vendor management, and financial tracking.

### **How EMS Works**
The EMS project follows a structured workflow:

1. **Create a Group**
   - Groups act as a collection of related events.
   - Each event must belong to a group.

2. **Add Multiple Events to a Group**
   - Once a group is created, users can add multiple events under it.
   - Each event has details like date, type, budget, and description.

3. **Add Service and Support Products (SSP)**
   - SSPs are services, setups, and products needed for an event.
   - Categories include Furniture, Decor, Stage, Lighting, and more.

4. **Add Vendors**
   - Vendors provide services for the event.
   - Each vendor has a name, service type, contact information, and pricing.

5. **Associate SSPs and Vendors with Events**
   - SSPs and Vendors can be assigned to an event.
   - The system tracks assignments and their details.

6. **Record Payments and Vendor Transactions**
   - Users can log payments for vendors.
   - The system maintains a financial record for each vendor’s services.

7. **Event Creation Flow (Automated Workflow)**
   - A step-by-step event planning tool.
   - Users select SSPs through an interactive slideshow.
   - The system generates a final quotation.
   - A beautifully formatted PowerPoint presentation is created.

---

## EMS (Event Management System) - Features Overview

EMS is designed to provide a complete solution for event managers. The system covers every aspect of event management from planning to execution, ensuring that every detail is tracked and managed efficiently. Below is a detailed list of features that empower event managers to handle all aspects of their events.

## Core Features

- **User Authentication & Account Management**
  - Secure user registration, login, and logout.
  - Password recovery and profile management.
  - Role-based access control for different user types.

- **Group Management**
  - Create and manage groups to organize events.
  - Add multiple events under a single group.
  - Edit group details and track overall group progress.

- **Event Management**
  - Add, edit, and delete events within groups.
  - Detailed event scheduling with dates, descriptions, and budgets.
  - Real-time event status updates and event tracking.
  - Comprehensive management dashboard for an overview of all events.

## Service and Product Management

- **SSP (Service and Support Products) Management**
  - Add and manage products, services, and setups required for events.
  - Categorize SSPs for easy filtering (e.g., Furniture, Decor, Lighting).
  - Assign SSPs to events and track quantities and usage.

- **Vendor Management**
  - Maintain a complete database of vendors with contact details, service types, ratings, and pricing.
  - Assign vendors to specific events and tasks.
  - Edit vendor profiles and update service details.
  - Track vendor performance and feedback.

- **Venue Management**
  - Manage venue details including location, capacity, and layout recommendations.
  - Input and update venue-specific requirements.
  - Coordinate venue booking and associated logistics.

## Financial and Transaction Features

- **Payment and Financial Tracking**
  - Record and monitor vendor payments and invoice histories.
  - Track event budgets, extra costs, and overall financial summaries.
  - Maintain detailed payment histories for audit and accountability.
  - Generate financial reports and export them as PDF or Excel.

## Event Creation and Workflow Automation

- **Event Creation Flow**
  - Interactive, step-by-step event creation process.
  - Slideshow-based selection of SSPs to facilitate a guided setup.
  - Final review of event details including selected products, services, and venue information.
  - Generate a final quotation based on selected components.

- **Automated PPT Generation**
  - Automatically generate professional PowerPoint presentations summarizing event details.
  - Include key information such as event objectives, SSP selections, vendor assignments, and quotations.
  - Quick and easy export for client presentations and internal reviews.

## Reporting, Notifications, and Dashboard

- **Reports & Analytics**
  - Generate event progress reports, vendor performance summaries, and financial overviews.
  - Export reports in multiple formats (PDF, Excel).
  - Visual analytics on event metrics and key performance indicators.

- **Notification & Alert System**
  - In-app notifications for upcoming deadlines, pending tasks, and vendor updates.
  - Email alerts for critical actions such as payment due dates and event modifications.

- **Comprehensive Dashboard**
  - Overview of all active events, groups, and tasks.
  - Quick access to key metrics and recent activity logs.
  - Customizable dashboard widgets for personalized insights.

## Additional Features

- **Task and Assignment Management**
  - Create and assign tasks related to events.
  - Calendar view to track task deadlines and progress.
  - Audit trail for changes in event assignments and vendor management.

- **Customization and Settings**
  - Dark/Light mode toggle for user interface personalization.
  - Detailed user settings for account preferences and notification management.
  - Support for multi-user collaboration with distinct permissions.

- **Integration and Extensibility**
  - Modular design to allow integration with third-party systems and APIs.
  - Future-proof architecture to support additional modules and functionalities.
  - Secure data management ensuring compliance with data protection standards.

- **Security & Compliance**
  - Encrypted communication and secure data storage.
  - Regular updates to maintain system security and user privacy.
  - Detailed logs for audit and compliance purposes.

This comprehensive set of features makes EMS a powerful tool for event managers to streamline planning, execution, and post-event analysis, ensuring every event is managed with precision and efficiency.



## Running the Project

1. **Launch the server:**
   ```bash
   python manage.py runserver
   ```
2. **Navigate the system:**
   - Start by logging in or registering a user.
   - Create a group and add events.
   - Assign SSPs and vendors to an event.
   - Track payments and generate event reports.
   - Use the event creation flow to finalize event details and generate a quotation & PPT.

---

## Project Structure

The project is organized into several Django apps:

*   **accounts**: Manages user accounts, authentication, and authorization.
*   **core**: Contains the core functionality of the EMS, including event, group, and SSP (Service and Support Product) management.
*   **event_creation**: Handles the event creation workflow.

## Core Django Files

*   **manage.py**: A command-line utility for interacting with the Django project. It provides commands for running the development server, executing database migrations, and more.
*   **ems/settings.py**: Contains the project's settings, such as database configuration, installed apps, middleware, and more.
*   **ems/urls.py**: Defines the project's URL patterns, mapping URLs to views.
*   **ems/wsgi.py**: A WSGI (Web Server Gateway Interface) entry point for deploying the project to a production web server.
*   **ems/asgi.py**: An ASGI (Asynchronous Server Gateway Interface) entry point for deploying the project with asynchronous capabilities.

## Apps Analysis

### accounts App

The accounts app manages user accounts, authentication, and authorization.

#### Models

The `accounts` app uses Django's built-in User model for managing user accounts. No custom models are defined in this app.

#### URLs

*   `/login/`: Displays the login form. Uses Django's built-in `LoginView`.
*   `/logout/`: Logs the user out. Uses Django's built-in `LogoutView`.
*   `/signup/`: Displays the signup form and handles user registration.
*   `/home/`: Displays the home page for logged-in users.

#### Views

*   `signup(request)`: Handles user registration. If the form is submitted and valid, it saves the user and redirects to the login page.
*   `home(request)`: Renders the home page (`home.html`) for logged-in users. Requires the user to be logged in; otherwise, redirects to the login page.

### core App

The core app contains the core functionality of the EMS, including event, group, and SSP (Service and Support Product) management.

#### Models

*   `Ssp`: Represents a Service and Support Product, with fields like `item_id`, `name`, `rate_per_event`, `tags`, `item_type`, and `image`.
*   `Event`: Represents an event, with fields like `event_id`, `event_name`, `group` (ForeignKey to `Group`), `event_type`, `date`, `budget`, `description`, and `ssps` (ManyToManyField to `Ssp` through `EventSsp`).
*   `EventSsp`: Represents the relationship between an event and an SSP, with fields like `event` (ForeignKey to `Event`), `ssp` (ForeignKey to `Ssp`), and `quantity`.
*   `Vendor`: Represents a vendor, with fields like `vendor_id`, `vendor_name`, `service_type`, `contact_info`, `rating`, `rate_per_event`, and `details`.
*   `Group`: Represents a group, with fields like `group_id`, `group_name`, `client` (ForeignKey to `Client`), `date`, `budget`, `status`, and `reports` (ManyToManyField to `Report`).
*   `Client`: Represents a client, with fields like `client_id`, `client_name`, `contact_email`, and `contact_phone`.
*   `Task`: Represents a task, with fields like `task_id`, `task_name`, `event` (ForeignKey to `Event`), `assigned_to` (ForeignKey to `Vendor`), `status`, `deadline`, and `is_reminder`.
*   `VendorEventAssignment`: Represents the assignment of a vendor to an event, with fields like `vendor` (ForeignKey to `Vendor`), `event` (ForeignKey to `Event`), `task` (ForeignKey to `Task`), `role_description`, `budget`, `date_assigned`, `payment_status`, `status`, `payment_history`, and `work_payment_mapping`.
*   `Report`: Represents a report, with fields like `report_id`, `event` (ForeignKey to `Event`), `report_type`, `created_by` (ForeignKey to `User`), `created_at`, `data`, and `file_path`.

#### URLs

*   `/login/`: Displays the login form. Uses Django's built-in `LoginView`.
*   `/logout/`: Logs the user out. Uses Django's built-in `LogoutView`.
*   `/get_events/<int:group_id>/`: Returns a JSON response containing the events for a given group.
*   `/`: Displays the home page.
*   `/add_ssp/`: Adds an SSP to the database.
*   `/event/sge_ssp/`: Selects a group and event for SSP management.
*   `/event/<int:event_id>/ssps/`: Lists the SSPs associated with an event.
*   `/event/<int:event_id>/link_ssps/`: Links SSPs to an event.
    *   `/event/<int:event_id>/update_ssp_quantity/<int:item_id>/`: Updates the quantity of an SSP linked to an event.
    *   `/event/<int:event_id>/remove_ssp/<int:item_id>/`: Removes an SSP from an event.
*   `/events/`: Displays the groups dashboard (also events dashboard).
*   `/all_ssps/`: Displays all SSPs in the database.
    *   `/update_all_ssps/`: Updates all SSPs in the database.
    *   `/remove_ssp/<int:ssp_id>/`: Removes an SSP from the database.
*   `/group/add/`: Adds a new group.
*   `/group/<int:group_id>/edit_group_details/`: Edits group details.
*   `/group/<int:group_id>/manage/`: Manages a group (displays associated events).
*   `/group/<int:group_id>/add_event/`: Adds an event to a group.
*   `/event/<int:event_id>/edit/`: Edits an event.
*   `/event/<int:event_id>/manage/`: Manages an event.
*   `/vendor/add/`: Adds a new vendor.
*   `/vendor/dashboard/`: Displays the vendor dashboard.
*   `/vendor/sge_vendor`: Select Group Event for vendor assignment
*   `/vendor/assign_vendor/`: Assigns a vendor to an event.
    *   `/vendor/<int:vendor_id>/edit_vendor/`: Edits a vendor.
    *   `vendor/manage_assignment/<int:assignment_id>/`: Manages vendor assignment
    *   `vendor/assignment_detail/<int:vendor_id>/`: Vendor assignment detail
    *   `vendor/record_payment/<int:assignment_id>/`: Record payment for vendor

#### Views

*   `get_events(request, group_id)`: Returns a JSON response containing the events for a given group.
*   `home(request)`: Renders the home page (`home.html`).
*   `add_ssp(request)`: Handles adding a new SSP.
*   `sge_ssp(request)`: Selects a group and event for SSP management.
*   `link_ssp_to_event(request, event_id)`: Handles linking SSPs to an event.
*   `event_ssp_list(request, event_id)`: Lists the SSPs associated with an event.
*   `update_ssp_quantity(request, event_id, item_id)`: Updates the quantity of an SSP linked to an event.
*   `remove_ssp_from_event(request, event_id, item_id)`: Removes an SSP from an event.
*   `all_ssps(request)`: Lists all SSPs.
*   `update_all_ssps(request)`: Updates all SSPs.
*   `remove_ssp(request, ssp_id)`: Removes an SSP.
*   `add_group(request)`: Handles adding a new group.
*   `edit_group_details(request, group_id)`: Handles editing group details.
*   `manage_group(request, group_id)`: Manages a group (displays associated events).
*   `add_event(request, group_id)`: Handles adding an event to a group.
*   `edit_event(request, event_id)`: Handles editing an event.
*   `manage_event(request, event_id)`: Manages an event.
*   `add_vendor(request)`: Handles adding a new vendor.
*   `vendor_dashboard(request)`: Displays the vendor dashboard.
*   `edit_vendor(request, vendor_id)`: Handles editing a vendor.
*   `sge_vendor(request)`: Select Group Event for vendor assignment
*   `assign_vendor(request)`: Assigns a vendor to an event.
    *   `manage_assignment(request, assignment_id)`: Manages vendor assignment
    *   `assignment_detail(request, vendor_id)`: Vendor assignment detail
    *   `record_payment(request, assignment_id)`: Record payment for vendor

### event_creation App

The event_creation app handles the event creation workflow.

#### Models

The `event_creation` app does not define any custom models.

#### URLs

*   `/dashboard/<int:event_id>/`: Displays the dashboard for a specific event.
*   `/start_flow/<int:event_id>/`: Starts the event creation flow for a specific event.
*   `/category_flow/<int:event_id>/<str:category_name>/`: Displays the category flow page for a specific event and category.
*   `/summary/<int:event_id>/`: Displays the summary page for a specific event.
*   `/quotation/<int:event_id>/`: Displays the quotation page for a specific event.
*   `/generate_ppt/<int:event_id>/`: Generates a PowerPoint presentation for a specific event.

#### Views

*   `dashboard_ec(request, event_id)`: Renders the dashboard for the event creation process.
*   `start_flow(request, event_id)`: Redirects to the first category in the event creation flow.
*   `category_flow(request, event_id, category_name)`: Handles the selection of SSPs for a given category in the event creation flow.
*   `summary(request, event_id)`: Displays a summary of the selected SSPs for the event.
*   `quotation(request, event_id)`: Generates a quotation for the event based on the selected SSPs.
*   `generate_ppt(request, event_id)`: Generates a PowerPoint presentation summarizing the event details and selected SSPs.

## Static Files

The static directory contains static files such as CSS, JavaScript, and images.

## Media Files

The media directory contains user-uploaded media files, such as SSP images and PPT files.

---


## Conclusion

EMS is designed to streamline event planning with an intuitive and structured workflow. It simplifies the process of organizing events, assigning services, tracking finances, and generating professional reports. Follow the steps above to get started, and explore the system to plan and manage your events efficiently!

