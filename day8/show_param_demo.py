"""show 参数赋值演示脚本

展示: 默认值、位置参数、关键字参数、与可变参数组合、重复赋值错误示例。
运行: python day8/show_param_demo.py
"""


def show(
    a,
    b=3,
    c=5,
    *args,
    **kwargs,
):
    print(f"a={a}, b={b}, c={c}, args={args}, kwargs={kwargs}")


def main():
    print("示例 1：只传 a（使用 b 和 c 的默认值）")
    show(1)
    print()

    print("示例 2：用位置参数给 b 和 c（第三个位置是 c）")
    show(1, 2, 3)
    print()

    print("示例 3：用关键字给 c（显式）")
    show(1, 2, c=9)
    print()

    print("示例 4：省略 b，用关键字给 c（b 使用默认值）")
    show(1, c=3)
    print()

    print("示例 5：多余的位置参数进入 args，同时有 kwargs")
    show(1, 2, 3, 4, 5, d=9)
    print()

    print(
        "示例 6：错误示例 — 同时用位置和关键字给 c（会抛 TypeError），我们捕获并显示异常"
    )
    try:
        # 这里第三个位置已经给 c 赋值为 3，下面再用 c=9 会导致重复赋值
        show(1, 2, 3, c=9)
    except TypeError as e:
        print("捕获到异常：", type(e).__name__, e)


if __name__ == "__main__":
    main()
