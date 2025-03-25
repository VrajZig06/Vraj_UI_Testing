from datetime import datetime

# Open a report file when the test suite starts
def before_all(context):
    context.report_file = open("Test_Report.txt", "w")
    context.report_file.write("=== Cucumber Test Report ===\n\n")

# Capture the start time before each scenario
def before_scenario(context, scenario):
    context.scenario_start_time = datetime.now()
    context.scenario_error = None  # Reset error tracking

    # Write scenario name at the start
    context.report_file.write(f"Scenario: {scenario.name}\n")

# Log each step as it is executed
def after_step(context, step):
    step_status = "passed" if step.status == "passed" else "failed"

    # Log the step name and its status
    context.report_file.write(f"    {step.keyword} {step.name} [{step_status}]\n")
    
    # Capture any error that occurs in the step
    if step.status == "failed":
        context.scenario_error = str(step.exception)

# Log each scenario's status, including duration
def after_scenario(context, scenario):
    end_time = datetime.now()
    duration = (end_time - context.scenario_start_time).total_seconds()
    scenario_status = "passed" if scenario.status == "passed" else "failed"

    context.report_file.write(f"Status: {scenario_status}\n")
    context.report_file.write(f"Execution Time: {duration:.2f} seconds\n")

    if scenario_status == "failed" and context.scenario_error:
        context.report_file.write(f"Error: {context.scenario_error}\n")

    context.report_file.write("--------------------------------------------------\n\n")

# Close the report file when the test suite finishes
def after_all(context):
    if hasattr(context, 'report_file'):
        context.report_file.close()




# from driver import get_driver
# from appium import webdriver

# def before_all(context):
#     try:
#         context.driver = webdriver.Remote('http://localhost:4723/wd/hub', load_capabilities)
#     except Exception as e:
#         print(f"Failed to initialize driver: {e}")
#         context.failed = True

# def after_all(context):
#     if hasattr(context, 'driver') and context.driver:
#         context.driver.quit()


# from driver import get_driver

# def before_all(context):
#     try:
#         # Initialize the driver using the get_driver function
#         context.driver = get_driver()
#     except Exception as e:
#         print(f"Failed to initialize driver: {e}")
#         context.failed = True

# def after_all(context):
#     if hasattr(context, 'driver') and context.driver:
#         context.driver.quit()
