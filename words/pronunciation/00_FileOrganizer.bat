@echo off
setlocal enabledelayedexpansion

REM 步骤1：创建26个字母文件夹（a-z）
for %%i in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
    if not exist "%%i" (
        mkdir "%%i"
        echo 已创建文件夹: %%i
    )
)

REM 步骤2：按首字母移动文件
for %%f in (*.*) do (
    if not "%%f"=="%~nx0" (  REM 跳过脚本自身
        set "filename=%%f"
        set "firstChar=!filename:~0,1!"  REM 提取首字母
        set "firstChar=!firstChar!"  REM 转为小写（注：批处理无内置转小写，需额外处理）
        for %%c in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do (
            if /i "!firstChar!"=="%%c" (  REM /i忽略大小写匹配
                move "%%f" "%%c\" >nul 2>&1
                echo 已移动 "%%f" -> %%c\
            )
        )
    )
)
echo 文件分类完成！
pause