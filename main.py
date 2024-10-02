def all_targets_hit_upgrade(attempts: list) -> bool:
    return all(any(attempt) for attempt in attempts)

attempts = [
  [True, False, True],
  [False, False, True],
  [False, False],
 ]

