# Enterprise-Scale Sales Data Analytics Project

## Overview

This project demonstrates the end-to-end process of building an enterprise-grade sales data analytics system using Python, Snowflake, SQL, and Power BI. The goal was to simulate a large-scale sales ecosystem, replicate real-world data complexities, and provide business decision-makers with actionable insights through interactive dashboards.

## Key Features

- Engineered a scalable, relational dataset with over **1 million transactional records** across multiple tables, including `FactOrder`, `dimCustomer`, `dimProduct`, `dimStore`, `dimDate`, and `dimLoyaltyInfo`.
- Performed **ETL (Extract, Transform, Load)** operations by writing 20+ optimized **SQL queries** for data cleaning, joins, and aggregations.
- Integrated **Snowflake** with **Power BI** to streamline data flow, perform further transformations in Power Query, and create dynamic measures using DAX.
- Built a comprehensive **executive dashboard** in Power BI visualizing key business metrics like:
  - Revenue trends
  - Customer loyalty impact
  - Product category performance
  - Regional sales patterns

## Technologies Used

- **Python**: For dataset simulation and automation tasks.
- **Snowflake**: Cloud data warehousing for scalable data storage and processing.
- **SQL**: Writing optimized queries for ETL processes, data transformation, and aggregation.
- **Power BI**: For creating interactive dashboards and data visualizations.
- **DAX**: For building calculated columns and custom KPIs in Power BI.
- **Power Query**: For additional transformations after Snowflake data integration.

## Data Model

The data model simulates an enterprise sales ecosystem using a star schema, with a central **Fact Table** and several **Dimension Tables**:

- **FactOrder**: Contains transactional data such as order amounts, order dates, and product IDs. This is the central fact table linking to various dimensions.
- **dimCustomer**: Stores customer data including customer IDs, demographics (e.g., age, income group), and region information (e.g., country, state).
- **dimProduct**: Stores product details including product IDs, categories (e.g., electronics, clothing), and pricing information.
- **dimStore**: Contains store-level data, including store IDs, location (e.g., city, region), and store performance (e.g., sales by store).
- **dimDate**: Includes date-related information such as day, month, quarter, year, and fiscal periods. It enables time-based analysis like year-over-year and month-over-month comparisons.
- **dimLoyaltyInfo**: Contains loyalty program details for customers, such as membership level, loyalty points, and rewards eligibility, which helps in analyzing the impact of customer loyalty on sales.

## Project Breakdown

### 1. **Data Simulation**

A simulated dataset representing an enterprise-grade sales environment was created by using Python Fake data Library generating over **1 million transactional record** across various fact and dimension tables. These datasets replicate real-world complexities and reflect the typical relationships in sales ecosystems.

### 2. **ETL Pipeline using SQL and Snowflake**

- **Extract**: Raw data was simulated and loaded into Snowflake using stages.
- **Transform**: Applied various data transformations including:
  - Data cleaning (removing duplicates, handling nulls)
  - Complex SQL joins between fact and dimension tables
  - Aggregations to calculate key business metrics
- **Load**: Data was loaded into Snowflake tables and made available for further analysis.

### 3. **Power BI Integration**

- Connected Snowflake with Power BI to retrieve the data for analysis.
- Used **Power Query** for additional transformations and **DAX** for creating calculated columns and measures.
- Developed an **interactive dashboard** that visualizes key business insights, allowing stakeholders to track revenue trends, assess customer loyalty, and analyze product and regional sales performance.

### 4. **Executive Dashboard**

The dashboard provides an interactive interface for tracking KPIs:
- **Revenue Trends**: Track sales performance over time.
- **Customer Loyalty Impact**: Assess how customer loyalty influences sales metrics.
- **Product Category Performance**: View performance breakdown by product categories.
- **Regional Sales Patterns**: Analyze how sales vary by region.
