## 2026-05-13 - Added visual feedback for async network requests
**Learning:** CLI tools often stall silently during network requests (e.g., fetching a Facebook page to extract a user ID). This can look like the app froze.
**Action:** Always add a visual progress/loading indicator (e.g., 'Fetching profile details...') before executing slow synchronous network calls to improve user experience.

## 2026-05-13 - Fallback for terminal size calculation
**Learning:** Using `os.get_terminal_size()` crashes the application when run in non-interactive environments or when input/output is piped, leading to an `OSError: [Errno 25] Inappropriate ioctl for device`.
**Action:** Use `shutil.get_terminal_size()` instead, as it safely falls back to a default size (typically 80x24) when a real terminal is unavailable, making the CLI more resilient.

## 2024-05-24 - CLI Input Handling and URL Validation
**Learning:** Failing to strip whitespace from user inputs or validate empty inputs leads to confusing errors later. Overly strict URL validation (like only checking for `/videos/`) can cause false positives for valid Facebook URLs (like `/watch` or `/reel/`).
**Action:** Always strip CLI inputs, handle empty states gracefully with clear error messages, and ensure validation logic accurately reflects all valid input formats.

## 2026-05-13 - Standardizing Exit Commands and Formatting Numbers
**Learning:** Users instinctively try to exit CLI apps using 'q', 'quit', or 'exit', rather than reading specific numeric options for exiting. Additionally, large unformatted numbers (like view counts) are hard to parse visually and slow down reading comprehension.
**Action:** Always accept standard exit strings ('q', 'quit', etc.) alongside any numeric options, and format large numeric metrics with commas (e.g., `1,234,567`) to improve visual hierarchy and readability.
