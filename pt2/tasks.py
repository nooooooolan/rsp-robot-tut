from robocorp.tasks import task
from robocorp import browser
from robocorp import files  

from RPA.HTTP import HTTP

@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    open_robot_order_website()
    download_csv()
    orders = get_orders()
    
    return


def open_robot_order_website():
    browser.goto("https://robotsparebinindustries.com")

def download_csv():
    http = HTTP()
    http.download("https://robotsparebinindustries.com/orders.csv", "orders.csv", overwrite=True)
        
def get_orders():
    orders = files.read_csv("orders.csv")
    return orders

def close_annoying_modal():
    page=browser.page()
    page.click("text=OK")

def fill_the_form():
    orders = get_orders()
    page = browser.page()
    
    head_names = {
        "1" : "Roll-a-thor body",
        "2" : "Peanut crusher body",
        "3" : "D.A.V.E. body",
        "4" : "Andy Roid body",
        "5" : "Spanner mate body",
        "6" : "Drillbit 2000 body"
    }
    head_number = order["head"]
    
    page.select_option("head", head_names.get(head_number))
    
    
    
    for order in orders:
        browser.fill("id=head", order["head"])
        browser.sele