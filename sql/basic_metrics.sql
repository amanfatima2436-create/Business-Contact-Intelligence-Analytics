-- ============================================
-- Business Contact Intelligence Analytics
-- Basic Business Metrics
-- ============================================

-- 1. Total Number of Contacts
SELECT
    COUNT(*) AS total_contacts
FROM business_contacts;


-- 2. Total Unique Companies
SELECT
    COUNT(DISTINCT law_firms_name) AS unique_companies
FROM business_contacts;


-- 3. Contacts with Phone Number
SELECT
    COUNT(phone_number) AS contacts_with_phone
FROM business_contacts;


-- 4. Contacts with Email
SELECT
    COUNT(email) AS contacts_with_email
FROM business_contacts;


-- 5. Contacts with Complete Contact Information
SELECT
    COUNT(*) AS complete_contacts
FROM business_contacts
WHERE contact_completeness = 2;