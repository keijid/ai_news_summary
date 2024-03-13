# AI News Summary

AI News Summaryは、人工知能に関するニュース記事を自動的に要約し、Slackに通知するプロジェクトです。

## 概要

このプロジェクトは、以下の機能を提供します：

- 指定されたRSSフィードからニュース記事を定期的に取得
- OpenAI APIを使用して、各記事の要約を生成
- 生成された要約をSlackチャンネルに通知

## 使用技術

- Python
- Google Cloud Functions
- Google Cloud Scheduler
- Google Cloud Pub/Sub
- OpenAI API
- Slack Incoming Webhook

## セットアップ

1. Google Cloud Functionsを設定し、`main.py`をデプロイします。
2. OpenAI APIキーとSlack Incoming Webhook URLを環境変数として設定します。
3. Google Cloud Pub/Subトピックを作成します。
4. Google Cloud SchedulerにCron jobを設定し、Pub/Subトピックにメッセージを発行します。

## ファイル構成

- `main.py`: Cloud Functionsのエントリーポイント。ニュース記事の取得、要約、Slack通知を行います。
- `requirements.txt`: 必要なPythonパッケージを記載したファイル。
- `README.md`: プロジェクトの説明文書。

## 貢献

このプロジェクトへの貢献は大歓迎です。改善点や新機能のアイデアがある場合は、Issueを作成するかプルリクエストをお送りください。

## ライセンス

このプロジェクトは[MIT License](LICENSE)の下で公開されています。

## 連絡先

- 名前: [あなたの名前]
- Email: [あなたのメールアドレス]
- GitHub: [あなたのGitHubアカウント]
