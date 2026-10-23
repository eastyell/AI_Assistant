"""
MCP 远程服务端 (Streamable HTTP 模式)
"""
import datetime
from mcp.server.fastmcp import FastMCP
# from mcp.server.mcpserver import MCPServer
import functionTools as ft

# 创建 MCP 服务实例
mcp = FastMCP(name="RemoteDemoServer", host="192.168.0.103")

# ==================== 定义工具 ====================

@mcp.tool()
def get_current_time() -> str:
    """获取服务器当前的日期和时间。"""
    now = datetime.datetime.now()
    return f"服务器当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}"

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """计算两个整数的和。
    
    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b

@mcp.tool()
def get_package(express_name, tracking_number: str) -> str:
    '''
      调用物流API，获取快递的物流状态
      参数express_name为快递公司名称
      参数tracking_number为快递单号
      返回值：快递的物流状态
    '''
    return ft.get_package(express_name, tracking_number)

@mcp.tool()
def send_email(tostr, subject, body, files_path=[]):
    '''
      调用邮件API，发送邮件
      参数tostr为收件人邮箱地址
      参数subject为邮件主题
      参数body为邮件正文
      参数files_path为附件路径列表
      返回值：邮件发送结果
    '''
    return ft.send_email(tostr, subject, body, files_path)
@mcp.tool()
def search_knowledge_base(query: str) -> str:
    """在学校知识库中搜索相关信息。当用户询问学校规章制度、课程安排、招生信息、专业设置、校园生活等学校相关问题时，调用此工具。"""
    return ft.search_knowledge_base(query)

# ==================== 启动服务 ====================

if __name__ == "__main__":
    print("🚀 MCP 远程服务端启动中...")
    print("📡 监听地址: http://192.168.0.103:8000/mcp")
    print("等待客户端连接...\n")
    
    # ⭐️ 核心：使用 streamable-http 传输模式
    mcp.run(transport="streamable-http")