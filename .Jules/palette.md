## 2026-05-13 - Added visual feedback for async network requests
**Learning:** CLI tools often stall silently during network requests (e.g., fetching a Facebook page to extract a user ID). This can look like the app froze.
**Action:** Always add a visual progress/loading indicator (e.g., 'Fetching profile details...') before executing slow synchronous network calls to improve user experience.

## 2026-05-13 - Fallback for terminal size calculation
**Learning:** Using `os.get_terminal_size()` crashes the application when run in non-interactive environments or when input/output is piped, leading to an `OSError: [Errno 25] Inappropriate ioctl for device`.
**Action:** Use `shutil.get_terminal_size()` instead, as it safely falls back to a default size (typically 80x24) when a real terminal is unavailable, making the CLI more resilient.

## 2024-05-24 - CLI Input Handling and URL Validation
**Learning:** Failing to strip whitespace from user inputs or validate empty inputs leads to confusing errors later. Overly strict URL validation (like only checking for `/videos/`) can cause false positives for valid Facebook URLs (like `/watch` or `/reel/`).
**Action:** Always strip CLI inputs, handle empty states gracefully with clear error messages, and ensure validation logic accurately reflects all valid input formats.

## 2026-05-19 - Graceful Exit on Empty Inputs
**Learning:** CLI tools that throw hostile red error messages (e.g., "Error: No URL provided.") when a user submits an empty input can make users feel penalized for simply changing their mind or wanting to back out of a menu option.
**Action:** Treat empty inputs in sub-menus as a deliberate "Cancel/Back" action. Provide a friendly yellow message (e.g., "Operation cancelled. Returning to main menu.") and explicitly hint this in the prompt (e.g., "or press Enter to cancel").

## 2026-05-19 - Reducing cognitive load with CLI screen clears
**Learning:** Endless scrolling in CLI menus quickly leads to a cluttered terminal, making it difficult for users to track where they are or focus on the current task.
**Action:** Implement screen clearing (e.g., `os.system('cls' if os.name == 'nt' else 'clear')`) between distinct task states and when looping back to the main menu to maintain a clean, focused workspace and reduce cognitive load.
