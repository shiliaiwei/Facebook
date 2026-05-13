## 2026-05-13 - Added visual feedback for async network requests
**Learning:** CLI tools often stall silently during network requests (e.g., fetching a Facebook page to extract a user ID). This can look like the app froze.
**Action:** Always add a visual progress/loading indicator (e.g., 'Fetching profile details...') before executing slow synchronous network calls to improve user experience.

## 2026-05-13 - Fallback for terminal size calculation
**Learning:** Using `os.get_terminal_size()` crashes the application when run in non-interactive environments or when input/output is piped, leading to an `OSError: [Errno 25] Inappropriate ioctl for device`.
**Action:** Use `shutil.get_terminal_size()` instead, as it safely falls back to a default size (typically 80x24) when a real terminal is unavailable, making the CLI more resilient.
