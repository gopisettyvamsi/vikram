# Functional Documentation
## AI Test Case Generator - User Guide

**Version:** 1.0.0
**For:** QA Engineers, Test Managers, Business Analysts
**Last Updated:** December 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [User Interface Guide](#user-interface-guide)
4. [Generating Test Cases](#generating-test-cases)
5. [Understanding Test Case Types](#understanding-test-case-types)
6. [Viewing & Analyzing Results](#viewing--analyzing-results)
7. [Exporting Test Cases](#exporting-test-cases)
8. [Best Practices](#best-practices)
9. [Use Cases & Examples](#use-cases--examples)
10. [FAQs](#faqs)
11. [Tips & Tricks](#tips--tricks)

---

## Overview

### What is AI Test Case Generator?

The AI Test Case Generator is an intelligent tool that automatically creates comprehensive test cases for your software modules, APIs, and web pages using artificial intelligence. It saves time, ensures coverage, and maintains consistency in test case creation.

### Key Benefits

✅ **Time Saving**: Generate dozens of test cases in seconds
✅ **Comprehensive Coverage**: Includes functional, negative, boundary, and security tests
✅ **Consistency**: Standardized format and structure
✅ **Professional Quality**: Industry-standard test case documentation
✅ **Multiple Formats**: Export to JSON, CSV, Excel, or Text
✅ **Easy to Use**: No technical expertise required

### Who Should Use This Tool?

- **QA Engineers**: Create test cases for sprint planning
- **Test Managers**: Quickly generate test suites for new features
- **Business Analysts**: Document acceptance criteria as test cases
- **Developers**: Generate unit and integration test scenarios
- **Product Managers**: Validate feature requirements

---

## Getting Started

### Accessing the Application

1. **Launch the Application**:
   ```bash
   streamlit run ui.py
   ```

2. **Open Your Browser**:
   Navigate to: `http://localhost:8501`

3. **Verify Access**:
   - Your IP must be whitelisted
   - You'll see the main dashboard if authorized
   - Contact admin if you see "Access Denied"

### First-Time Setup

No setup required for users! The application is ready to use immediately.

---

## User Interface Guide

### Main Dashboard

```
┌──────────────────────────────────────────────────────────┐
│                                                           │
│           🧪 AI Test Case Generator                       │
│     Generate comprehensive, AI-powered test cases         │
│                    in seconds                             │
│                                                           │
├──────────────────────────────────────────────────────────┤
│                                                           │
│   📝 Describe Your Module                                │
│   ┌─────────────────────────────────────────────────┐   │
│   │ Enter description here...                        │   │
│   │                                                   │   │
│   └─────────────────────────────────────────────────┘   │
│                                                           │
│               [🚀 Generate Test Cases]                    │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

### Sidebar Information

The left sidebar shows:

- **About**: Application information
- **Features**: Types of test cases generated
- **Export Formats**: Available download formats
- **Statistics**: Real-time metrics (after generation)
- **IP Address**: Your current IP status

---

## Generating Test Cases

### Step 1: Describe Your Module

In the text area, provide a clear description of what you want to test.

**What to Include:**

- Module/page/API name
- Key functionalities
- Input fields and their types
- Actions (buttons, links, etc.)
- Expected behaviors
- Special requirements

**Example Input:**

```
Login page with the following elements:
- Email input field (accepts email format only)
- Password input field (minimum 8 characters)
- "Remember Me" checkbox
- "Forgot Password?" link
- "Login" button
- Social login options (Google, Facebook)
- Show/hide password toggle icon
```

### Step 2: Click Generate

Click the **"🚀 Generate Test Cases"** button.

**What Happens:**
1. AI analyzes your description
2. Identifies test scenarios
3. Generates comprehensive test cases
4. Displays results in multiple views

**Processing Time:** Usually 5-15 seconds depending on complexity.

### Step 3: Review Results

Once generated, you'll see:

- ✅ Success banner with total count
- 📊 Metrics showing breakdown by type
- 📋 Test cases in your chosen view
- 💾 Export options

---

## Understanding Test Case Types

### 1. Functional Test Cases

**Purpose**: Verify that features work as intended

**Example**:
```
ID: TC-001
Title: Valid login with correct credentials
Type: Functional
Steps:
  1. Navigate to login page
  2. Enter valid email address
  3. Enter correct password
  4. Click "Login" button
Expected Result: User successfully logged in and redirected to dashboard
```

### 2. Negative Test Cases

**Purpose**: Verify system handles invalid inputs correctly

**Example**:
```
ID: TC-015
Title: Login with invalid email format
Type: Negative
Steps:
  1. Navigate to login page
  2. Enter invalid email (e.g., "usertest.com")
  3. Enter password
  4. Click "Login" button
Expected Result: Error message "Invalid email format" displayed
```

### 3. Boundary Test Cases

**Purpose**: Test edge cases and limits

**Example**:
```
ID: TC-022
Title: Password with exactly 8 characters
Type: Boundary
Steps:
  1. Navigate to registration page
  2. Enter password with exactly 8 characters
  3. Submit form
Expected Result: Password accepted (minimum boundary test)
```

### 4. Security Test Cases

**Purpose**: Verify security measures

**Example**:
```
ID: TC-030
Title: SQL injection attempt in email field
Type: Security
Steps:
  1. Navigate to login page
  2. Enter SQL injection string in email field
  3. Click "Login" button
Expected Result: Input sanitized, injection prevented
```

---

## Viewing & Analyzing Results

### View Options

#### 📊 Table View

- **Best For**: Quick overview of all test cases
- **Features**:
  - Sortable columns
  - Compact display
  - Easy scanning
  - Steps count visible

**Columns**:
- ID
- Title
- Type
- Scenario (truncated)
- Steps (count)
- Status

#### 📄 Detailed View

- **Best For**: Reading full test case details
- **Features**:
  - Expandable sections
  - Color-coded badges by type
  - Complete steps visible
  - Full scenario descriptions

#### 🔍 JSON View

- **Best For**: Technical review, API integration
- **Features**:
  - Raw JSON format
  - Complete data structure
  - Easy to copy
  - Programmatic access

### Statistics Dashboard

After generation, the sidebar shows:

```
📈 Statistics
Total Test Cases: 25
Functional: 12
Negative: 8
Boundary: 3
Security: 2
```

Use these metrics to:
- Assess coverage balance
- Identify gaps
- Report to stakeholders

---

## Exporting Test Cases

### Available Formats

#### 📥 JSON Format

**Best For**: API integration, automation frameworks

**Structure**:
```json
{
  "module": "Login page...",
  "total_test_cases": 25,
  "test_cases": [...]
}
```

**Use Cases**:
- Import into test management tools
- Automation script generation
- Data analysis

#### 📥 CSV Format

**Best For**: Excel manipulation, reporting

**Columns**:
- ID
- Title
- Scenario
- Type
- Steps (semicolon-separated)
- Expected Result
- Status

**Use Cases**:
- Import into TestRail, Jira, etc.
- Create custom reports
- Data filtering and sorting

#### 📥 Excel (XLSX) Format

**Best For**: Documentation, presentations

**Features**:
- Formatted headers
- Auto-adjusted column widths
- Professional appearance
- Color-coded status (future use)

**Use Cases**:
- Test plan documentation
- Stakeholder presentations
- Team distribution

#### 📥 Text Format

**Best For**: Documentation, printing

**Format**:
```
AI TEST CASE GENERATOR
=================================

MODULE: Login page
TOTAL TEST CASES: 25
GENERATED: 2025-12-10 14:30:00
=================================

[TC-001] Valid login test
-------------------------
Type: Functional
Scenario: User logs in...
Steps:
  1. Navigate to login page
  2. Enter valid credentials
  ...
Expected Result: ...
Status: Pending
=================================
```

**Use Cases**:
- Printing
- Email distribution
- Simple documentation

### How to Export

1. **Generate Test Cases** (if not already done)
2. **Scroll to Export Section** (below test cases)
3. **Click Your Preferred Format**:
   - 📥 JSON
   - 📥 CSV
   - 📥 Excel
   - 📥 Text
4. **File Downloads Automatically** to your Downloads folder

**Filename Format**: `test_cases.[ext]`

---

## Best Practices

### Writing Good Module Descriptions

#### ✅ DO:

```
User Registration Form with:
- First Name and Last Name fields (text, required)
- Email field (email format validation)
- Password field (min 8 chars, 1 uppercase, 1 number)
- Confirm Password field (must match password)
- Terms & Conditions checkbox (required)
- Submit button
- Validation messages for each field
```

#### ❌ DON'T:

```
registration form
```

### Description Guidelines

1. **Be Specific**: Include field names, types, and validations
2. **Include Actions**: Mention buttons, links, and interactions
3. **Mention Validations**: Describe any rules or constraints
4. **Add Context**: Explain the purpose if needed
5. **Use Clear Language**: Avoid jargon unless necessary

### Optimal Description Length

- **Minimum**: 50 characters
- **Optimal**: 150-300 characters
- **Maximum**: 500 characters

### What to Include

✅ Input fields and their properties
✅ Actions (buttons, links)
✅ Validation rules
✅ Expected behaviors
✅ Special features (dropdowns, modals, etc.)
✅ Integration points (APIs, third-party services)

### What to Avoid

❌ Vague descriptions
❌ Implementation details
❌ Code snippets
❌ Too much irrelevant context
❌ Multiple unrelated features in one request

---

## Use Cases & Examples

### Use Case 1: E-Commerce Checkout

**Input**:
```
Checkout page for e-commerce website:
- Shipping address form (name, street, city, zip, country)
- Payment method selection (credit card, PayPal, bank transfer)
- Credit card form (number, expiry, CVV)
- Order summary section showing items and total
- Promo code input field
- "Place Order" button
- Form validations for all required fields
```

**Output**: 20-25 test cases covering:
- Valid checkout flow
- Address validation
- Payment method validation
- Promo code application
- Form error handling
- Boundary cases for amounts
- Security checks for card data

### Use Case 2: REST API Endpoint

**Input**:
```
POST /api/users endpoint for user creation:
- Accepts JSON body with: username, email, password
- Username must be unique and 3-20 characters
- Email must be valid format
- Password must be 8+ characters with special char
- Returns 201 on success with user object
- Returns 400 on validation error
- Returns 409 if username/email exists
- Requires API key in header
```

**Output**: 18-22 test cases covering:
- Successful user creation
- Invalid input validation
- Duplicate checking
- Authentication
- Response codes
- Edge cases

### Use Case 3: Search Functionality

**Input**:
```
Search feature on product page:
- Search input field (text)
- Search button
- Auto-suggestions dropdown while typing
- Filters: category, price range, rating
- Sort options: relevance, price, newest
- Results display with pagination
- "No results found" message for empty searches
```

**Output**: 15-20 test cases covering:
- Basic search functionality
- Filter application
- Sorting mechanisms
- Pagination
- Empty state handling
- Special character handling

---

## FAQs

### Q1: How many test cases are generated?

**A**: Typically 15-30 test cases depending on complexity. The AI determines optimal coverage.

### Q2: Can I edit the generated test cases?

**A**: Yes! Export to your preferred format and edit freely. The exported files are standard formats.

### Q3: Are the test cases ready to use?

**A**: Yes! They follow industry-standard format and can be used directly or imported into test management tools.

### Q4: What if I don't like some test cases?

**A**: Simply delete unwanted cases from the exported file. You can also regenerate with a modified description.

### Q5: Can I generate test cases for multiple modules at once?

**A**: Currently, generate one module at a time. However, you can describe multiple related features in one description.

### Q6: How accurate are the test cases?

**A**: The AI is trained on industry best practices. However, review and customize based on your specific requirements.

### Q7: Can I save my session?

**A**: Export your test cases to save them. The session clears on page refresh.

### Q8: What happens if generation fails?

**A**: You'll see an error message. Simply try again. If it persists, simplify your description.

### Q9: Can I use this for mobile app testing?

**A**: Yes! Describe mobile screens and interactions just like web pages.

### Q10: Is there a limit on how many times I can generate?

**A**: No limits for whitelisted IPs. Generate as many times as needed.

---

## Tips & Tricks

### 💡 Tip 1: Start Simple

For complex modules, start with a basic description and regenerate with more details if needed.

### 💡 Tip 2: Use Examples

Include example values in your description:
```
Email field (e.g., user@example.com)
Phone field (format: +1-XXX-XXX-XXXX)
```

### 💡 Tip 3: Mention Error Messages

If you know specific error messages, include them:
```
Email validation error: "Please enter a valid email address"
```

### 💡 Tip 4: Group Related Features

Instead of "login form", write:
```
Authentication module including login form, password reset,
and remember me functionality
```

### 💡 Tip 5: Specify Test Data

Mention what test data should be used:
```
Test with: valid user, invalid user, blocked user
```

### 💡 Tip 6: Review All View Types

Check all three views (Table, Detailed, JSON) to ensure completeness before exporting.

### 💡 Tip 7: Export Multiple Formats

Export to both Excel (for documentation) and JSON (for automation).

### 💡 Tip 8: Customize Post-Export

Feel free to add:
- Priority levels
- Assigned testers
- Prerequisites
- Test data specifics

### 💡 Tip 9: Use for Sprint Planning

Generate test cases at the start of sprint to estimate testing effort.

### 💡 Tip 10: Share with Stakeholders

Export to Excel and share with PMs/BAs for requirement validation.

---

## Common Workflows

### Workflow 1: Sprint Planning

1. **Before Sprint**: Generate test cases for upcoming features
2. **During Sprint Planning**: Estimate testing effort
3. **Assign**: Distribute test cases to team
4. **Execute**: Update status in exported file
5. **Report**: Use statistics for reporting

### Workflow 2: Bug Verification

1. **Bug Fixed**: Generate test cases for the fixed component
2. **Review**: Ensure regression scenarios are covered
3. **Execute**: Run all generated test cases
4. **Document**: Attach test results to bug ticket

### Workflow 3: API Testing

1. **API Docs**: Review API specification
2. **Generate**: Create test cases from API description
3. **Automate**: Use JSON export for test automation
4. **Integrate**: Import into automation framework

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Focus input | Click in text area |
| Submit | Ctrl + Enter (in text area) |
| Scroll down | Page Down |
| Scroll up | Page Up |

---

## Support & Feedback

### Need Help?

- **Technical Issues**: Contact IT support
- **Feature Requests**: Submit via feedback form
- **Training**: Schedule session with QA lead

### Feedback

We welcome your feedback! Let us know:
- What works well
- What could be improved
- Feature suggestions
- Bug reports

---

## Glossary

| Term | Definition |
|------|------------|
| **Functional Test** | Tests that verify features work as intended |
| **Negative Test** | Tests that verify proper handling of invalid inputs |
| **Boundary Test** | Tests at the limits of acceptable inputs |
| **Security Test** | Tests for vulnerabilities and security measures |
| **Test Case** | A set of conditions and steps to verify functionality |
| **Expected Result** | The anticipated outcome of test execution |
| **Actual Result** | The real outcome after test execution |
| **Test Status** | Current state (Pending, Pass, Fail) |

---

## Quick Reference Card

### 📝 How to Generate

1. Describe module
2. Click "Generate"
3. Review results
4. Export

### 📊 View Types

- **Table**: Quick overview
- **Detailed**: Full information
- **JSON**: Raw data

### 💾 Export Formats

- **JSON**: Automation
- **CSV**: Spreadsheets
- **Excel**: Documentation
- **Text**: Printing

### ✅ Best Practices

- Be specific
- Include validations
- Mention error messages
- Add examples
- Review before export

---

## Appendix A: Sample Test Case Structure

```
Test Case ID: TC-001
Title: Brief descriptive title (3-8 words)
Scenario: Detailed description of what is being tested
Type: Functional | Negative | Boundary | Security
Steps:
  1. First action
  2. Second action
  3. Third action
  ...
Expected Result: What should happen
Status: Pending | Passed | Failed
```

---

## Appendix B: Integration Guide

### TestRail Integration

1. Export as CSV
2. In TestRail: Import > CSV
3. Map columns to TestRail fields
4. Import

### Jira Integration

1. Export as CSV
2. In Jira: Import > CSV
3. Create custom field mapping
4. Import as Test cases

### Manual Integration

1. Export to Excel
2. Copy-paste into your tool
3. Format as needed

---

**Document Version**: 1.0.0
**Last Updated**: December 10, 2025
**For Questions**: Contact QA Team Lead

---

**Happy Testing! 🧪**
