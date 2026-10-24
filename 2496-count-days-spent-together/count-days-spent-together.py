class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
      days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

      def convert_to_day_number(date_str: str) -> int:
        month, day = map(int, date_str.split("-"))
        return sum(days_in_months[: month - 1]) + day

      alice_arrive = convert_to_day_number(arriveAlice)
      alice_leave = convert_to_day_number(leaveAlice)
      bob_arrive = convert_to_day_number(arriveBob)
      bob_leave = convert_to_day_number(leaveBob)

      # The overlap period starts on the later arrival date and ends on the earlier leave date
      overlap_arrive = max(alice_arrive, bob_arrive)
      overlap_leave = min(alice_leave, bob_leave)

      # Calculate total overlapping days (inclusive)
      # If overlap_arrive > overlap_leave, they don't overlap, so return 0
      return max(0, overlap_leave - overlap_arrive + 1)