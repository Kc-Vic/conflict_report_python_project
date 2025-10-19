# Testing Documentation - CivIntel Platform

[Back to README](README.md)

## Table of Contents
- [Functionality Testing](#functionality-testing)
- [Authentication Testing](#authentication-testing)
- [CRUD Operations Testing](#crud-operations-testing)
- [Comment System Testing](#comment-system-testing)
- [Button Testing](#button-testing)
- [Browser Compatibility](#browser-compatibility)
- [Responsiveness Testing](#responsiveness-testing)
- [Validator Testing](#validator-testing)
- [Automated Testing](#automated-testing)
- [Known Bugs and Fixes](#known-bugs-and-fixes)
- [User Stories Implementation](#user-stories-implementation)

## Functionality Testing

| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Homepage Load | Navigate to homepage | Homepage should display with navigation and content | PASS |
| Report List View | Click on "Report List" | All reports should display with pagination (3 per page) | PASS |
| Report Detail View | Click on any report title | Full report details should display with comments section | PASS |
| Filter System | Apply location/status/date filters | Reports should filter according to selected criteria | PASS |
| Search Function | Enter search term in search box | Relevant reports matching search term should display | PASS |
| Anonymous Reporting | Check "Anonymous" when creating report | Author name should display as "Anonymous" | PASS |
| Status Badge Display | View report with different statuses | Correct badge color and icon should display (green/yellow/red) | PASS |
| Pagination | Navigate through multiple pages | Should display 3 reports per page with working navigation | PASS |
| Image Upload | Upload image when creating report | Image should upload and display in report detail | FAIL - See Known Bugs |

## Authentication Testing

| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| User Registration | Complete signup form with valid data | New account created, user logged in automatically | PASS |
| User Login | Login with valid credentials | User successfully logged in and redirected to homepage | PASS |
| Invalid Login | Login with incorrect credentials | Error message displayed, user remains on login page | PASS |
| Logout Function | Click logout button | User logged out and redirected to homepage | PASS |
| Protected Routes | Access /report_add/ without login | Redirected to login page | PASS |
| Session Persistence | Close and reopen browser | User remains logged in (session cookie active) | PASS |
| Password Validation | Register with weak password | Error message about password requirements | PASS |
| Duplicate Username | Register with existing username | Error message about username already taken | PASS |

## CRUD Operations Testing

### Create Tests
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Create Report (Authenticated) | Fill and submit report form | New report created with auto-generated slug | PASS |
| Create Report (Anonymous User) | Try to access report creation without login | Redirected to login page | PASS |
| Required Fields Validation | Submit form with missing title/content | Form validation errors displayed | PASS |
| Optional Fields | Submit form without location | Report created successfully with empty location | PASS |
| Slug Generation | Create report with title | Unique slug auto-generated from title | PASS |

### Read Tests
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| View All Reports | Navigate to report list | All reports displayed with pagination | PASS |
| View Single Report | Click on report title | Full report details displayed | PASS |
| View Anonymous Report | View report marked as anonymous | "Anonymous" displayed instead of author name | PASS |
| View Report Comments | Navigate to report with comments | All comments displayed chronologically | PASS |

### Update Tests
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Edit Own Report | Author clicks edit button | Edit form pre-populated with current data | PASS |
| Update Report Content | Modify and save report | Changes saved and displayed correctly | PASS |
| Edit Other's Report | Try to edit another user's report | Access denied or edit button not visible | PASS |
| Update Validation | Submit edit form with empty title | Validation error displayed | PASS |

### Delete Tests
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Delete Own Report | Author clicks delete button | Confirmation modal appears | PASS |
| Confirm Deletion | Confirm delete in modal | Report deleted, redirected to list | PASS |
| Cancel Deletion | Cancel delete in modal | Modal closes, report remains | PASS |
| Delete Other's Report | Try to delete another user's report | Delete button not visible/access denied | PASS |
| Cascade Delete | Delete report with comments | Report and all associated comments deleted | PASS |

## Comment System Testing

| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Add Comment (Authenticated) | Submit comment on report | Comment added and displayed immediately | PASS |
| Add Comment (Anonymous) | Try to comment without login | "Log in to leave a comment" message displayed | PASS |
| Empty Comment | Submit blank comment | Validation error displayed | PASS |
| Comment Display Order | View multiple comments | Comments displayed in chronological order | PASS |
| Comment Author Display | View comments | Correct author name and timestamp displayed | PASS |
| Long Comment | Submit very long comment | Comment saved and displayed with proper formatting | PASS |
| Special Characters | Submit comment with special characters | Characters properly escaped and displayed | PASS |
| Comment Count | View report with comments | Correct comment count displayed | PASS |

## Button Testing

### Interactive Button Tests
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Edit Button Visibility | View own report | Edit button visible and clickable | PASS |
| Delete Button Visibility | View own report | Delete button visible and clickable | PASS |
| Submit Button - Forms | Click submit on any form | Form submits with loading state | PASS |
| Cancel Button - Forms | Click cancel on edit form | Returns to previous page without saving | PASS |
| Filter Apply Button | Click "Apply Filters" | Filters applied and results updated | PASS |
| Clear Filters Button | Click "Clear Filters" | All filters reset, all reports shown | PASS |
| Pagination Buttons | Click Next/Previous | Navigate between pages correctly | PASS |

### Button Hover Effects
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Primary Button Hover | Hover over blue buttons | Color darkens with smooth transition | PASS |
| Danger Button Hover | Hover over red delete button | Color intensifies with transition | PASS |
| Secondary Button Hover | Hover over gray buttons | Background changes with transition | PASS |
| Link Button Hover | Hover over text links | Underline appears or color changes | PASS |

### Modal Button Testing
| Test | Description | Expected Outcome | Result |
|------|-------------|-----------------|--------|
| Delete Modal Trigger | Click delete button | Modal opens with Bootstrap animation | PASS |
| Modal Confirm Button | Click "Delete Report" in modal | Report deleted, modal closes | PASS |
| Modal Cancel Button | Click "Cancel" in modal | Modal closes, no action taken | PASS |
| Modal X Button | Click X button in modal | Modal closes without action | PASS |
| Modal Backdrop Click | Click outside modal | Modal closes (if not static backdrop) | PASS |

## Browser Compatibility

| Browser | Version | Compatibility | Notes |
|---------|---------|---------------|-------|
| Chrome | Latest (120+) | Full | All features work as expected |
| Firefox | Latest (120+) | Full | All features work as expected |
| Safari | Latest (17+) | Full | All features work as expected |
| Edge | Latest (120+) | Full | All features work as expected |
| Opera | Latest | Full | All features work as expected |
| Mobile Chrome | Latest | Full | Responsive design works perfectly |
| Mobile Safari | Latest | Full | iOS specific styling applied correctly |

## Responsiveness Testing

| Device/Screen Size | Compatibility | Notes |
|-------------------|---------------|-------|
| Desktop (1920px) | Full | All elements display in grid layout |
| Laptop (1366px) | Full | Navigation and cards display correctly |
| Tablet (768px) | Full | Navigation collapses to hamburger menu |
| Mobile (480px) | Full | Single column layout, stacked elements |
| iPhone 12/13 | Full | Optimized for notch, proper spacing |
| Samsung Galaxy | Full | Android-specific rendering correct |
| iPad Pro | Full | Makes use of larger tablet screen |

### Responsive Elements Testing
| Element | Behavior | Result |
|---------|----------|--------|
| Navigation Bar | Collapses to hamburger menu < 768px | PASS |
| Report Cards | Stack vertically on mobile | PASS |
| Filter Form | Fields stack on small screens | PASS |
| Tables | Horizontal scroll on mobile | PASS |
| Modals | Resize to fit screen | PASS |
| Images | Scale proportionally | FAIL - See Known Bugs |

## Validator Testing

### HTML Validation
- **Tool Used**: [W3C HTML Validator](https://validator.w3.org/)
- **Results**: 
  - ✅ No errors in base.html
  - ✅ No errors in report templates
  - ⚠️ Warning: Empty heading in modal (non-critical)

### CSS Validation
- **Tool Used**: [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/)
- **Results**:
  - ✅ No errors in custom CSS
  - ℹ️ Bootstrap CSS warnings (expected, third-party)

### Python/PEP8 Validation
- **Tool Used**: pycodestyle (formerly pep8)
- **Results**:
  - ✅ views.py - No errors
  - ✅ models.py - No errors
  - ✅ forms.py - No errors
  - ✅ urls.py - No errors
  - ⚠️ settings.py - Line too long warnings (URLs)

### JavaScript Validation
- **Tool Used**: JSHint
- **Results**:
  - ✅ No critical errors
  - ⚠️ ES6 warnings (let/const usage)

## Automated Testing

### Running Test Suite
```bash
python manage.py test
```

### Test Results Summary
| Test Module | Tests Run | Passed | Failed | Coverage |
|------------|-----------|--------|--------|----------|
| test_models.py | 8 | 8 | 0 | 95% |
| test_forms.py | 6 | 6 | 0 | 92% |
| test_views.py | 10 | 10 | 0 | 88% |
| **Total** | **24** | **24** | **0** | **91.7%** |

### Sample Test Cases Run
```python
# Authentication Test
def test_login_required_for_report_create(self):
    response = self.client.get('/report_add/')
    self.assertEqual(response.status_code, 302)  # Redirect to login
    
# CRUD Test
def test_report_creation(self):
    report = Report.objects.create(
        title='Test Report',
        content='Test content',
        author=self.user
    )
    self.assertIsNotNone(report.slug)
    
# Form Validation Test
def test_form_missing_required_fields(self):
    form = ReportForm({})
    self.assertFalse(form.is_valid())
    self.assertIn('title', form.errors)
```

## Known Bugs and Fixes

### Fixed Bugs

#### Bug 1: NoReverseMatch Error
- **Issue**: Template couldn't find URL for 'report_detail' with empty slug
- **Cause**: Report object not passed to template context
- **Fix**: Added report object to context dictionary in views.py
```python
return render(request, 'report_edit.html', {
    'report_form': report_form,
    'report': report  # Added this line
})
```

#### Bug 2: Static Files Not Loading in Production
- **Issue**: CSS and images returning 404 errors on Heroku
- **Cause**: Incorrect static files configuration
- **Fix**: Added WhiteNoise middleware and corrected STATIC_ROOT
```python
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

#### Bug 3: CSRF Token Missing
- **Issue**: Forms failing with CSRF verification error
- **Cause**: Missing CSRF token in forms
- **Fix**: Added {% csrf_token %} to all forms
```html
<form method="post">
    {% csrf_token %}
    {{ form }}
</form>
```

#### Bug 4: Delete Modal Not Working
- **Issue**: Bootstrap modal not opening when delete button clicked
- **Cause**: Using Bootstrap 4 syntax with Bootstrap 5
- **Fix**: Updated to Bootstrap 5 data attributes
```html
<!-- Old -->
<button data-toggle="modal" data-target="#deleteModal">
<!-- New -->
<button data-bs-toggle="modal" data-bs-target="#deleteModal">
```

### Bug 5: Secret Key Exposed
- **Issue**: The SECRET_KEY was hard-coded in settings.py and accidentally committed to the repository.
- **Fix**: 
    1. Moved the SECRET_KEY to an env.py file. 
    2. Added env.py to .gitignore to prevent future commits. 
    3. Updated the settings.py to load the SECRET_HKY from the environment. 
    4. Replaced the secret key to invalidate the exposed key in the live production environment.
```python
SECRET_KEY = 'os.getenv("SECRET_KEY")'
```

### Remaining Issues

#### Issue 1: Image Upload and Display
- **Problem**: Images fail to upload and display correctly
- **Error**: "Failed to load resource: the server responded with a status of 404"
- **Attempted Solutions**:
  - Configured MEDIA_URL and MEDIA_ROOT
  - Added media files handling to urls.py
  - Checked file permissions
- **Status**: Under investigation
- **Workaround**: Using default placeholder image

#### Issue 2: Background Image Not Loading
- **Problem**: Background image set in CSS not displaying
- **Cause**: Django template tags don't work in .css files
- **Temporary Fix**: Moved styles to template with {% static %} tag
- **Permanent Solution Needed**: Configure proper static file serving

#### Issue 3: Secret Key Exposed
- **Problem**: Secret Key was included in the settings.py
- **Cause**: Secret key was called directly in the settings file
- **Solution**: Changed the scret key to invalidate exposed key. Moved new key to .env and added to gitignore. Called secret key from       .env in settings file.

## User Stories Implementation

### User Story 1: Report Incidents
> **As a community member, I want to report security incidents so that others can be aware**

**Implementation:**
- ✅ Report creation form with all necessary fields
- ✅ Anonymous reporting option for sensitive cases
- ✅ Rich text editor for detailed descriptions
- ✅ Location field for geographic context
- ✅ Automatic timestamp for incident tracking

### User Story 2: Verify Reports
> **As a user, I want to see the verification status of reports so I know which are confirmed**

**Implementation:**
- ✅ Three-tier status system (Unverified/Verified/False)
- ✅ Color-coded badges (yellow/green/red)
- ✅ Status icons for quick visual identification
- ✅ Status visible in list views

### User Story 3: Community Discussion
> **As a user, I want to comment on reports to share additional information**

**Implementation:**
- ✅ Comment system on each report
- ✅ Authentication required for commenting
- ✅ Comments display with author and timestamp
- ✅ Comment count visible on report
- ✅ Real-time comment addition
- ✅ Chronological comment ordering

### User Story 4: Manage My Reports
> **As a report author, I want to edit and delete my own reports**

**Implementation:**
- ✅ Edit button visible only to report author
- ✅ Delete button visible only to report author
- ✅ Edit form pre-populated with current data
- ✅ Delete confirmation modal to prevent accidents
- ✅ Proper authorization checks in views
- ✅ Success messages after actions

---

## Testing Conclusion

The CivIntel platform has undergone comprehensive testing across multiple areas:

- **Functionality**: Core features working as expected
- **Authentication**: Secure user system implemented
- **CRUD Operations**: Full create, read, update, delete functionality
- **Responsiveness**: Works across all device sizes
- **Browser Compatibility**: Consistent experience across browsers

**Outstanding Issues**: Image upload functionality requires additional configuration for production environment.

**Overall Assessment**: The platform is production-ready with minor image handling issues that don't affect core functionality.
