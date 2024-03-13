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

1. OpenAI APIキーとSlack Incoming Webhook URLを環境変数として設定します。
- `YOUR_OPENAI_API_KEY`をあなたのOpenAI APIキーに置き換えてください。
- `YOUR_SLACK_WEBHOOK_URL`をあなたのSlack Incoming Webhook URLに置き換えてください

2. Google Cloud Pub/Subトピックを作成します。
```
gcloud pubsub topics create news_summary_topic
```

3. Google Cloud Functionsを設定し、`main.py`をデプロイします。
```CLI
gcloud functions deploy news_summary --runtime python310 --trigger-topic news_summary_topic --set-env-vars OPENAI_API_KEY=YOUR_OPENAI_API_KEY,SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
```

4. Google Cloud SchedulerにCron jobを設定し、Pub/Subトピックにメッセージを発行します。
- Google Cloud Consoleで、Cloud Schedulerのページに移動します。
- 「ジョブを作成」をクリックし、必要な情報を入力します。
  - 名前：ジョブの名前を入力
  - 説明：ジョブの説明を入力
  - 頻度：Cron式で実行頻度を指定（例：`0 9 * * *`）
  - タイムゾーン：適切なタイムゾーンを選択
  - ターゲット：Pub/Subを選択
  - トピック：`news_summary_topic`を選択
  - ペイロード：任意のテキスト
- 「作成」をクリックしてジョブを作成します。

## ファイル構成

- `main.py`: Cloud Functionsのエントリーポイント。ニュース記事の取得、要約、Slack通知を行います。
- `requirements.txt`: 必要なPythonパッケージを記載したファイル。
- `README.md`: プロジェクトの説明文書。
