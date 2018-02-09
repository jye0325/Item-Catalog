# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.5.0] - 2018-02-07
### Added
- Added `CHANGELOG.md` documenting all changes and revisions.
- Added version tags to commits. 
- Added login/logout functions in `login.html` and `main.py` using Google OAuth api.
- Added protection in `main.py` to pages from unauthorized data entry/edit/deletion.

### Changed
- Changed commit: a0033e8 to its correct version, [v0.2.2].
- Updated tables in `database_setup.py` to incorporate User table and it's functions.
- Updated functions in `main.py` to incorporate login features.

### Removed
- Removed commit(s): d1d2d2b, 15e8466, c9861a2 from Master. These were
erronous commits in attempts to adding the `.gitignore` file in [v0.2.2].
- Removed `logout.html` file.

## [v0.4.0] - 2018-02-07
### Added
- Added jsonify functions and serializable properties to `main.py` and `database_setup.py`, respectively.
- Added preliminary login state to `main.py`.
- Added functionality to newCategory, deleteCategory, itemMenu, editItem, and deleteItem.

### Changed
- Removed Test User from `addDB.py`.
- Updated `delete.html` to include deleteItem functionality.
- Renamed `new.html`, `itemmenu.html`, `edit.html`, `delete.html` to its corresponding redirect_uri. Also added additional `.html` files necessary for other redirect_uris.
- Updated all the templates to perform it's corresponding functions.
- Minor revisions to `main.css`.

## [v0.3.1] - 2018-02-06
### Added
- Added editItem and deleteItem functions to `main.py`.

### Changed
- Updated `delete.html` to include deleteItem functionality.

### Fixed
- Minor bug fixes and corrections to `main.html`.

## [v0.3.0] - 2018-02-06
### Added
- Added `addDB.py` to test the program using a test database.
- Added `main.css` for preliminarily styling and layout of the webpages.

### Changed
- Modified `main.html` to display category and item entries, and map certain app routes.
This webpage was also modified to include `main.css` as it's styling sheet.
- Modified `main.py` for related functions to render templates for `main.html`.

## [v0.2.2] - 2018-02-05
### Added
- Added `.gitignore` to not include DS_Store.

## [v0.2.1] - 2018-02-05
### Added
- Added template files: `new.html`, `login.html`, `logout.html`, `itemmenu.html`,
`edit.html`, `delete.html`. These files however have no functions and 
serve only as placeholders.

- Added preliminary layout of information to be displayed on `main.html`.

### Changed
- Minor code revisions to `main.py`.

## [v0.2.0] - 2018-01-26
### Fixed
- Major bug fixes to `database_setup.py` and `main.py` that prevented initial 
release from executing.

## v0.1.0 - 2018-01-26
### Added
- Added initial database setup to `database_setup.py` file.
- Added routing and corresponding functions to `main.py` file.
- Added empty template to `main.html` file.

[Unreleased]: https://github.com/jye0325/Item-Catalog/compare/v0.5.0...HEAD
[v0.5.0]: https://github.com/jye0325/Item-Catalog/compare/v0.4.0...v0.5.0
[v0.4.0]: https://github.com/jye0325/Item-Catalog/compare/v0.3.1...v0.4.0
[v0.3.1]: https://github.com/jye0325/Item-Catalog/compare/v0.3.0...v0.3.1
[v0.3.0]: https://github.com/jye0325/Item-Catalog/compare/v0.2.2...v0.3.0
[v0.2.2]: https://github.com/jye0325/Item-Catalog/compare/v0.2.1...v0.2.2
[v0.2.1]: https://github.com/jye0325/Item-Catalog/compare/v0.2.0...v0.2.1
[v0.2.0]: https://github.com/jye0325/Item-Catalog/compare/v0.1.0...v0.2.0