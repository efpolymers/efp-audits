# 03_business_graph.md

# Enterprise Business Transformation Consulting Framework

## Business Graph Engine

**Version:** 1.0.0

------------------------------------------------------------------------

# Purpose

The Business Graph Engine reconstructs how an organization truly
operates.

Instead of viewing departments, software, documents, people, and
workflows independently, this module models the organization as a
connected graph of entities and relationships.

The graph becomes the single source of truth for downstream analysis.

------------------------------------------------------------------------

# Core Principles

-   Every business entity SHALL be represented as a node.
-   Every dependency SHALL be represented as a relationship.
-   Missing relationships SHALL be treated as investigation
    opportunities.
-   Recommendations SHALL consider upstream and downstream impacts.

------------------------------------------------------------------------

# Supported Entity Types

## Organizational

-   Company
-   Business Unit
-   Department
-   Team
-   Role
-   Employee
-   External Partner
-   Vendor
-   Government Authority

## Customer

-   Lead
-   Prospect
-   Client
-   Investor
-   Employee Applicant
-   Existing Customer
-   Returning Customer

## Operational

-   Workflow
-   Task
-   Approval
-   Decision
-   SLA
-   Exception
-   Escalation
-   Milestone

## Technology

-   CRM
-   ERP
-   HRMS
-   Accounting Software
-   Communication Platform
-   Storage System
-   AI Agent
-   Automation Workflow
-   API Integration

## Information

-   Document
-   Form
-   Template
-   Knowledge Base
-   Spreadsheet
-   Report
-   Dashboard

------------------------------------------------------------------------

# Required Node Attributes

Every node SHOULD contain where available:

-   Unique Identifier
-   Name
-   Category
-   Description
-   Owner
-   Department
-   Purpose
-   Inputs
-   Outputs
-   Dependencies
-   Systems Used
-   KPIs
-   Risks
-   Compliance Requirements
-   Source Evidence
-   Confidence Score

------------------------------------------------------------------------

# Relationship Types

The engine SHALL detect relationships including:

-   Reports To
-   Owns
-   Creates
-   Reviews
-   Approves
-   Consumes
-   Depends On
-   Triggers
-   Communicates With
-   Escalates To
-   Generates
-   Updates
-   Archives
-   Blocks
-   Replaces
-   Integrates With

Each relationship SHALL include:

-   Direction
-   Evidence
-   Confidence
-   Frequency
-   Business Impact

------------------------------------------------------------------------

# Business Graph Construction

The assistant SHALL progressively construct the graph using:

1.  Meeting transcripts
2.  SOPs
3.  Screenshots
4.  Process documents
5.  CRM exports
6.  Organizational charts
7.  System descriptions
8.  Clarification responses

Every new artifact SHALL refine the graph instead of replacing it.

------------------------------------------------------------------------

# Dependency Analysis

The engine SHALL identify:

-   Single Points of Failure
-   Circular Dependencies
-   Duplicate Responsibilities
-   Missing Owners
-   Manual Hand-offs
-   Shadow Systems
-   Bottlenecks
-   Compliance Dependencies
-   Founder Dependencies
-   Knowledge Dependencies

Each dependency SHALL be scored for operational risk.

------------------------------------------------------------------------

# Lifecycle Mapping

For every primary business process, map:

Lead → Qualification → Proposal → Payment → Onboarding → Delivery →
Quality Review → Customer Communication → Completion → Renewal → Support
→ Upsell

Highlight every ownership transfer and data handoff.

------------------------------------------------------------------------

# Business Graph Queries

The engine SHALL be capable of answering:

-   What breaks if this employee is unavailable?
-   Which workflows depend on this software?
-   Which approvals delay delivery?
-   Which documents are reused?
-   Which departments own customer communication?
-   Where is data duplicated?
-   Which systems are not integrated?
-   Which workflows lack clear ownership?

------------------------------------------------------------------------

# Gap Detection

Automatically detect:

-   Orphan workflows
-   Missing approvals
-   Undefined owners
-   Duplicate data entry
-   Untracked customer touchpoints
-   Missing KPIs
-   Missing documentation
-   Hidden manual work

Flag these for investigation or recommendation.

------------------------------------------------------------------------

# Graph Quality Rules

Before downstream modules execute, verify:

-   All core departments represented
-   Major workflows connected
-   Customer lifecycle complete
-   Technology mapped
-   Data movement understood
-   High-risk dependencies identified
-   Confidence assigned to major entities

If quality is insufficient, invoke the Clarification Protocol.

------------------------------------------------------------------------

# Output Contract

This module SHALL produce a structured Business Graph containing:

-   Entity catalogue
-   Relationship catalogue
-   Dependency map
-   High-risk nodes
-   Missing information list
-   Graph confidence summary

This output SHALL be consumed by:

-   Workflow Analysis
-   Technology Audit
-   Data Flow Analysis
-   Scoring Engine
-   Recommendation Engine
-   HTML Report Generator

The Business Graph SHALL remain the canonical representation of the
organization throughout the consulting engagement.
