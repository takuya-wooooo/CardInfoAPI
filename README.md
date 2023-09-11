# 🪪CardInfoAPI

## 🌟Features
様々なクレジットカードの特性情報（ポイント還元率、年会費など）を提供するAPI。

### 主な機能
・🎨 主な機能
・📋 カードの特性情報取得
・🏷 カードのカテゴリやタイプ
・🌟 利用者のレビューや評価
・🔍 カードの比較機能
・🔐 APIの認証
・📄 APIのページネーション
・🎛 APIのフィルタリング
・🧪 テスト
・📖 APIのドキュメンテーション(swagger)
・📝 ロギング
・🚨 モニタリング（Sentry）
・🛡 セキュリティ
・💾 バックアップ
・⏳ レートリミティング
・🚀 キャッシング

## 🛠Requirement
言語: Python3.11.5
フレームワーク: Django4.2.5, Django REST Framework3.14.0
DB: SQLite3.37.0

## 🔧Installation
```bash
pip install -r requirements.txt
```

## 🚀Usage
クレジットカード情報の取得
```bash
curl -X GET http://your-domain/cards/
```
特定のIDのクレジットカード情報を取得する場合:
```bash
curl -X GET http://your-domain/cards/1/
```

新しいクレジットカード情報の追加
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Test Card", "point_rate": 1.0, "annual_fee": 10000}' http://your-domain/cards/
```

クレジットカード情報の更新
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Test Card", "point_rate": 0.5, "annual_fee": 1100}' http://your-domain/cards/1/
```

クレジットカード情報の削除
```bash
curl -X DELETE http://your-api-domain/cards/1/
```

## 🗒Note
参考資料
・https://www.django-rest-framework.org/api-guide/settings/
・https://kakaku.com/card/