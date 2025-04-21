from datetime import datetime

def format_date(date_str):
    """Format date string to readable format"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%B %d, %Y • %I:%M %p")
    except:
        return date_str