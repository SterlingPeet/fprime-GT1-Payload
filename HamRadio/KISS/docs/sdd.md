# Amateur Radio KISS Packetizer Component

## 1. Introduction

Amateur Radio KISS format packetizer and depacketizer component for use within F Prime.

## 2. Requirements

The requirements for `HamRadio::KISSComponent` are as follows:

*Note:* Requirements are usually labelled with the initials of the component class, e.g. `CookieCutter -> CC-001`.

Requirement | Description | Verification Method
----------- | ----------- | -------------------
CC-001 | The `HamRadio::KISSComponent` component acknowledge ping requests | Unit Test
CC-002 | The `HamRadio::KISSComponent` component shall save the widgets | Unit Test

## 3. Design

### 3.1 Context

#### 3.1.1 Component Diagram

The `HamRadio::KISSComponent` component has the following component diagram:

![`HamRadio::KISSComponent` Diagram](img/KISSComponentBDD.jpg "HamRadio::KISSComponent")

#### 3.1.2 Ports

The `HamRadio::KISSComponent` component uses the following port types:

Port Data Type | Name | Direction | Kind | Usage
-------------- | ---- | --------- | ---- | -----
[`Svc::Fatal`](../Fatal/docs/sdd.html) | FatalReceive | Input | Synch | Receive FATAL notifications

### 3.2 Functional Description

(Lorum Ipsum) For Unix variants, it delays for one second before exiting with a segmentation fault. This allows time for the FATAL to propagate to the ground system so the user can see what event occurred and also generates a core for debugging (assuming ulimit is set correctly). For VxWorks, it suspends the calling thread. Projects can replace this component with another that does project-specific behavior like resets.

### 3.3 Scenarios

#### 3.3.1 FATAL Notification

The `HamRadio::KISSComponent` handles FATAL notifications:

![FATAL Notification](img/FatalNotification.jpg)

### 3.4 State

`HamRadio::KISSComponent` has no state machines (or does it?).

### 3.5 Algorithms

`HamRadio::KISSComponent` has no significant algorithms.

## 4. Dictionary

Dictionaries: [HTML](KISSComponent.html) [MD](KISS.md)

## 4. Module Checklists

Document            | Link
------------------- | ----
Design Checklist    | [Link](Checklist_Design.xlsx)
Code Checklist      | [Link](Checklist_Code.xlsx)
Unit Test Checklist | [Link](Checklist_Unit_Test.xls)

## 5. Unit Testing

[Unit Test Output](../test/ut/output/test.txt)

[Coverage Summary](../test/ut/output/HamRadioKISSComponent_gcov.txt)

[Coverage Output - `HamRadio::KISSComponent.cpp`](../test/ut/output/KISSComponent.cpp.gcov)

[Coverage Output - `KISSComponentAc.cpp`](../test/ut/output/KISSComponentAc.cpp.gcov)

## 6. Change Log

Date       | Description
---------- | -----------
10/13/2020 | Initial Component Design



