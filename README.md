# silent_sea_44703

## Table of Contents

1. [Project Description](#project-description)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
4. [Getting Started: Frontend](#getting-started-frontend)
   - [Installation](#installation)
   - [Running with Fastlane](#running-with-fastlane)
     - [Android](#android-1)
     - [iOS](#ios-1)
     - [React Native Web](#react-native-web)
5. [Getting Started: Backend](backend#readme)
6. [License](#license)

## Project Description

This react_native application was built with Crowdbotics www.crowdbotics.com

## Project Structure

    .
    ├── ...
    ├── android                 # Android native files
    ├── backend                 # Django backend REST API
    ├── ios                     # iOS native files
    ├── modules                 # Modules
    ├── public
    ├── screens
    ├── store                   # Application state storage
    ├── ...
    ├── README.md
    └── ...

## Modules (THIS SECTION IS AUTO-GENERATED, PLEASE DO NOT EDIT)

This section will show any installed modules you add from the Storyboard Modules section.

# Getting started: Frontend

This section outlines instructions on setting up a local development environment for the frontend of your application.

## Installation

### Metro

After cloning the repo, install the dependencies locally with [Yarn](https://yarnpkg.com/):

```sh
yarn install
```

Start your [Metro](https://facebook.github.io/metro/) server:

```sh
npx react-native start
```

### Android

```sh
npx react-native run-android
```

### iOS

```sh
pod install --repo-update --project-directory=ios
npx react-native run-ios
```

### Setup react-native-vector-icons

Follow instructions at their [README.md](https://github.com/oblador/react-native-vector-icons/blob/master/README.md#installation)

## Running with Fastlane

[Fastlane](https://fastlane.tools/) makes testing, building, and deploying apps
easier.

Install fastlane globally (`npm i -g fastlane` or `yarn i -g fastlane`).
Android and iOS dependencies are the same as React Native CLI.

All fastlane commands are run from the platform directory. For example, Android
commands must be run from `android/`. Fastlane should be executed using `bundle exec` to ensure dependencies are managed correctly.

The commands for Android and iOS are the same:

- Run tests: `bundle exec fastlane tests`
- Local build: `bundle exec fastlane build`
- Build and upload a beta (requires signing): `bundle exec fastlane beta`
- Build or promote a release: `bundle exec fastlane deploy`

### Android

Publish an Android app you must first create an app in the Play Console and
manually upload an APK. After the first upload run `bundle exec fastlane supply init` from `android/` to sync with the Play store. All future releases will be
uploaded automatically.

Android uses tracks. A beta release will build the app and upload to the beta
track. Deploying will promote from beta to production.

### iOS

CB developers must follow fastlane's [codesigning guide](https://codesigning.guide/) for using match.
Match will automatically sign iOS builds.

New CB developers should get access to the codesigning repo and run `bundle exec fastlane match development` from `ios/`.

Not a CB developer? Create an [Apple developer](https://developer.apple.com)
and follow the instructions on [codesigning guide](https://codesigning.guide/)
to setup your certificates.

## React Native Web

You can build and deploy your React Native app in the web too!

To get started run:

```sh
yarn run web
```

This will start a local development server so that you can iterate and preview your changes. Visit it at [localhost:8080](http://localhost:8080).

To build the web version of the project you can run:

```sh
yarn run web:build
```

And then commit/push the output created at `backend/web_build` to the git repository.

