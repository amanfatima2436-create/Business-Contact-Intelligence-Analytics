-- ============================================
-- Business Contact Intelligence Analytics
-- Lead Quality Analysis
-- ============================================


-- 1. Lead Quality Distribution
SELECT
    lead_quality,
    COUNT(*) AS total_leads
FROM business_contacts
GROUP BY lead_quality
ORDER BY total_leads DESC;


-- 2. Average Lead Quality Score
SELECT
    ROUND(AVG(lead_quality_score), 2) AS average_lead_quality_score
FROM business_contacts;


-- 3. High Quality Leads
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    email,
    phone_number,
    lead_quality_score
FROM business_contacts
WHERE lead_quality = 'High Quality Lead'
ORDER BY lead_quality_score DESC;


-- 4. Medium Quality Leads
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    email,
    phone_number,
    lead_quality_score
FROM business_contacts
WHERE lead_quality = 'Medium Quality Lead'
ORDER BY lead_quality_score DESC;


-- 5. Top 10 Highest Quality Leads
SELECT
    law_firms_name,
    first_name,
    last_name,
    title,
    lead_quality_score,
    lead_quality
FROM business_contacts
ORDER BY lead_quality_score DESC
LIMIT 10;
