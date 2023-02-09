class Solution:
    # Constant space and time
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        res = "{yyyy}-{mm}-{dd}"
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                  "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = day[:-2]
        return res.format(yyyy=year, mm=months[month], dd='0' + day if len(day) < 2 else day)
