# OJ Tourist
关于该项目：
- 为各大OJ平台中，你认为有意思的题目提供一份答案托管
- 旨在于让各位互相分享，互相监督，愉快且较有效率的刷题

## 代码结构
- output(存放各位已经ac的代码)
	- $(oj-platform-name)(ZOJ，code_war等)
		- $(platform-question-id)(在url中找独立编码)
			- README.md(用于题目描述)
			- $(your-username)
				- $(any-files-about-your-answers)
- utils(相关任务脚本)

## 提交注意点
- 在自己分支提交
- 目录结构格式不对，pr不会通过

## 考量中
目前的[ZOJ题库](./src/utils/questions.json)已经拿到，我在想是否需要自己架个task queue定期分发题目，再有一个监督机制，让各位像背单词一样的刷算法题。

## 祝刷题愉快
据说刷完1024题，天堂会有72个新垣结衣陪你跳舞
