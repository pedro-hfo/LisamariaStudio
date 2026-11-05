@appointments
Feature: Book time with the studio's only practitioner
  A session lasts 60 minutes and needs a 15-minute preparation buffer.
  These are learning examples, not approved business policies.

  @APT-001
  Scenario: Book an available time slot
    Given the practitioner has an empty schedule
    When I request an appointment at "2030-01-10T10:00:00+00:00"
    Then the appointment is accepted
    And the schedule contains 1 appointment

  @APT-002
  Scenario: Refuse an overlapping appointment
    Given an appointment starts at "2030-01-10T10:00:00+00:00"
    When I request an appointment at "2030-01-10T10:30:00+00:00"
    Then the time slot is unavailable
    And the schedule contains 1 appointment

  @APT-003
  Scenario: Preserve preparation time
    Given an appointment starts at "2030-01-10T10:00:00+00:00"
    When I request an appointment at "2030-01-10T11:00:00+00:00"
    Then the time slot is unavailable

  @APT-004
  Scenario: Book immediately after preparation finishes
    Given an appointment starts at "2030-01-10T10:00:00+00:00"
    When I request an appointment at "2030-01-10T11:15:00+00:00"
    Then the appointment is accepted
    And the schedule contains 2 appointments

  @APT-005
  Scenario: Refuse a past time slot
    Given the practitioner has an empty schedule
    When I request an appointment at "2029-12-31T10:00:00+00:00"
    Then the request is invalid
