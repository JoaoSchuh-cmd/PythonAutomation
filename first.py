import pyautogui

# print(pyautogui.position())

pyautogui.moveTo(18, 100)
pyautogui.click()
with pyautogui.hold('shift'):
    pyautogui.moveTo(87, 92)
    pyautogui.click()

pyautogui.hotkey('ctrlleft', 'C')

pyautogui.moveTo(974, 99)
pyautogui.click()
pyautogui.hotkey('ctrlleft', 'V')






