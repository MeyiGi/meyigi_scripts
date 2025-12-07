# Changelog

## [0.1.0] - 2024-03-16
### Added
- append to excel function added

## [0.2.0] - 2024-03-17
### Added
- timeit function for understand how long a function takes to execute

### Removed
- Deleted unnecessary dependencies from the required libraries.

## [0.3.0] - 2024-03-18
### Added
- get response from chatgpt added

## [0.4.0] - 2024-03-19
### Added
- get_requests function was added

### Removed
- removed unwanted dependencies for library

## [0.5.0] - 2024-03-20
### Added
- now we can make requests to gemini api to get str or dict

## [1.1.0] - 2024-03-21
### Added
- implemented append_to_json function which will append to json

### Changed
- was changed file structure of library for better importing

## [1.2.0] - 2024-03-22
### Added
- function which is cleaning texts was added

## [1.3.0] - 2024-03-23
### Added
- function which is retriying concrete times if appear errors

## [1.4.0] - 2024-03-24
### Added
- fucntion which is preventing fall asleep

## [1.4.1] - 2024-03-25
### Fixed
- fucntion which is preventing fall asleep

## [1.5.1] - 2024-03-25
### Added
- function which is downloading file with wget

## [1.5.2] - 2024-03-25
### Modified
- append_to_excel modified to work with lists

### Fixed
- get_requests timeout is working fine now

## [1.5.3] - 2024-03-25
### Modified
- append_to_json modified to work with lists

## [1.5.4] - 2024-04-01
### Added
- DocString for append_to_json
- DocString for append_to_excel
- DocString for clean_string
- DocString for get_requests
- DocString for download_file
- DocString for prevent_sleep

## [1.5.5] - 2024-04-01
### Added
- DocString for chatgpt_get_response
- DocString for generative

## [1.6.5] - 2024-04-01
### Added
- Added init_project fucntion which is will automatically init project

## [1.6.6] - 2024-04-01
### Fixed
- Dependencies should be contained
- init_project.main() -> init_project()

## [1.6.7] - 2024-04-07
### Fixed
- get_attributes function added

## [1.7.0] - 2024-04-08
### Fixed
- added scroll to bottom function


## [1.8.0] - 2024-04-10
### Fixed
- added get_item from product function

## [1.9.0] - 2024-04-12
### Fixed
- added load txt function
- added append to txt function

## [1.9.1] - 2024-04-13
### Modified
- get_attributes -> get_attribute: now we can send to this function either use list or one Tag

## [1.9.2] - 2024-04-13
### Modified
- append_to_txt modified now we can pass list

## [1.10.0] - 2024-04-15
### Added
- truncate_string function added

## [1.11.0] - 2024-04-15
### Added
- load_html_files function added

## [1.12.0] - 2024-04-21
### Added
- ColorPrinter class added

## [1.13.0] - 2024-04-22
### Added
- Generate filename function added

## [1.14.0] - 2024-04-24
### Added
- Setup Playwright function added
- get random headers function added

## [1.15.0] - 2024-04-27
### Added
- random_proxy function added
- random_delay function added
- get_selector function added

## [1.16.0] - 2024-04-28
### modified
- get_attribute now we can work with playwright elements

## [1.17.0] - 2025-06-01
### Added
- Browser protocol
- Playwright Undetected browser class


## [1.18.0] - 2025-06-01
### Added
- Wait min for elements added

## [2.0.0] - 2025-09-20
### Project Restructure & Imports: 
The library's internal file structure has been significantly reorganized into functional modules (ai, scraping, fileio, system, utils). While top-level imports via from meyigi_scripts import ... are preserved for convenience, direct imports will be broken.
### Asynchronous Playwright API: 
The PlaywrightUndetected class and browser utilities (setup_browser, wait_for_min_elements) now use an async API. All related function calls must be updated with await.
### Removed download_file Function: 
The legacy wget-based download_file function has been removed. All file downloads should now be handled through Playwright's native download capabilities, which are integrated into the PlaywrightUndetected class.
### Changed
#### Architectural Overhaul: Refactored the entire project into a more modular and maintainable structure with clear separation of concerns.
#### Switched all Playwright-based functions to an asynchronous API for significant performance improvements and to align with modern web automation practices.
### Removed
download_file function, to streamline the library and remove the wget dependency.


## [2.1.0] - 2025-09-20
### Added
- Read json function
- Read json folder function

## [2.1.1] - 2025-09-23
### Added
- Updated prevent_sleep function now it is moving mouse

## [2.1.2] - 2025-09-24
### Added
- Fixed import errors

## [2.1.3] - 2025-09-25
### Added
- Increased Robustness of prevent_sleep and get_random_headers functions

## [2.1.4] - 2025-09-28
### Added
- Removed init project garbage function
- load_txt function now with .strip() working right away for "list" return type
- docs(network): add typing + comment clarifying Desktop Chrome User-Agent in get_random_headers.

## [2.2.0] - 2025-09-29
### Added
- **Asynchronous HTTP Requests**: Introduced `get_async_requests` function in `meyigi_scripts.scraping.network`. This function uses `httpx` to perform high-concurrency, asynchronous GET requests, aligning with the library's `async` Playwright features.
- **CSV File Support**: Added a new `csv` module to `fileio` with `append_to_csv` and `read_csv` functions to handle reading and writing data in CSV format.

### Changed
- **Async Parser Utilities**: The `get_attribute` and `get_item` functions have been updated to include asynchronous support, ensuring full compatibility with the `async` Playwright API. *(This would be the next logical step to ensure consistency)*.

## [2.3.0] - 2025-09-30
### Added
- Read csv as dict program
- Append to csv program

## [2.3.1] - 2025-10-1
- fixed error that was not allowring to properly use library

## [2.3.2] - 2025-10-2
- removed unwanted library that was automatically installing to system "wget"

## [2.3.3] - 2025-10-3
- still was issues with wget but now it is fixed

## [2.4.0] - 2025-10-4
- added load_html_as_soup function that can handle either multiple files or single files 

## [2.0.1] - 2025-12-07
### Fixed
- Removed duplicate `read_csv_as_dicts` function from `excel_processor.py` which was incorrectly placed.