# Search and contact measurement

Canonical page: `https://pantani.xyz/triton-l200-hpe/`.
Search Console property: `sc-domain:pantani.xyz`.

## Search baseline

On 2026-10-03, the property's Performance report was still processing data.
No query volume, impressions, clicks, CTR, or average position baseline was
available. This is missing data, not measured zero demand.

After processing, filter Performance to the exact canonical page and Web search.
Export queries, pages, devices, and countries. Compare equal 28-day periods;
retain the migration/publication date when interpreting differences. Review
actual queries before changing copy. Group observed L200/Triton/HPE/HPE-S and
São Paulo variants for analysis without mislabeling the actual HPE-S vehicle.
Search Console does not provide a São Paulo state performance filter; do not
present country-level data as state-level demand.

## Contacts

No analytics collector or measurement ID was configured in the listing at this
audit. Do not introduce a fake ID or a local-only click counter: neither provides
reliable aggregate site measurement. Ask the owner for an existing analytics
property or a preferred provider before connecting collection.

Once configured, use a `whatsapp_click` event with a small allowlisted placement
value (`header`, `hero`, or `contact`). Do not send the phone number, message
text, buyer information, or arbitrary URL parameters as event properties.
Verify collection with a test event before claiming tracking works. Keep the
direct WhatsApp link functional when scripts are blocked or disabled.

A click is an outbound interaction, not a confirmed conversation, qualified
buyer, appointment, or sale. Track those later outcomes separately from the
owner's actual conversations, without publishing buyer details.

## Listing maintenance

Only add transmission, drivetrain, and service-document details after owner
confirmation. Keep price, mileage and sale status synchronized in visible copy
and structured data. No fictional city pages, delivery coverage or reviews.

## Sources

- https://support.google.com/webmasters/answer/7576553
- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes

This document defines a manual review procedure; no recurring automation was
requested or created.
