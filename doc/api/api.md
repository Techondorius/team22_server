# API Document

## イベント一覧取得 API

### リクエスト

```
GET /api/events
```

### レスポンス

#### 成功時

| param          | type   | description             |
| -------------- | ------ | ----------------------- |
| events[].id    | number | イベント ID             |
| events[].title | string | タイトル                |
| events[].owner | string | 主催者の名前            |
| events[].date  | Date   | 開催日時(ISO 8601 形式) |

```javascript
{
    "events": [
        {
            "id": number,
            "title": string,
            "owner": string,
            "date": Date
        },
        ...
    ]
}
```

## イベント詳細取得 API

### リクエスト

```
GET /api/events/{event_id}
```

### レスポンス

#### 成功時

| param | type   | description             |
| ----- | ------ | ----------------------- |
| id    | number | イベント ID             |
| title | string | タイトル                |
| owner | string | 主催者の名前            |
| date  | Date   | 開催日時(ISO 8601 形式) |
| note  | string | 詳細など                |
| url   | string | url                     |

```javascript
{
    "id": number,
    "title": string,
    "owner": string,
    "date": Date,
    "note": string,
    "url": string
}
```

### 失敗時

#### 対象が存在しない時

404 NotFound

## イベント登録 API

### リクエスト

```
POST /api/events/
```

| param      | type   | description             |
| ---------- | ------ | ----------------------- |
| title      | string | タイトル                |
| owner      | string | 主催者の名前            |
| date       | Date   | 開催日時(ISO 8601 形式) |
| note       | string | 詳細など                |
| url        | string | url                     |
| delete_key | string | 削除キー                |

```javascript
{
    "title": string,
    "owner": string,
    "date": Date,
    "note": string,
    "url": string,
    "delete_key": string
}
```

### レスポンス

#### 成功時

| param | type   | description             |
| ----- | ------ | ----------------------- |
| id    | number | イベント ID             |
| title | string | タイトル                |
| owner | string | 主催者の名前            |
| date  | Date   | 開催日時(ISO 8601 形式) |
| note  | string | 詳細など                |
| url   | string | url                     |

```javascript
{
    "id": number,
    "title": string,
    "owner": string,
    "date": Date,
    "note": string,
    "url": string
}
```

### 失敗時

#### パラメーターに問題がある場合

400 BadRequest

## イベント更新 API

一部パラメーターのみの変更も可能

### リクエスト

```
PUT /api/events/{event_id}
```

| param       | type   | description             |
| ----------- | ------ | ----------------------- |
| delete_key  | string | 削除キー                |
| event.title | string | タイトル                |
| event.owner | string | 主催者の名前            |
| event.date  | Date   | 開催日時(ISO 8601 形式) |
| event.note  | string | 詳細など                |
| event.url   | string | url                     |

```javascript
{
    "delete_key": string,
    "event": {
        "title": string,
        "owner": string,
        "date": Date,
        "note": string,
        "url": string,
    }
}
```

### レスポンス

#### 成功時

| param | type   | description             |
| ----- | ------ | ----------------------- |
| id    | number | イベント ID             |
| title | string | タイトル                |
| owner | string | 主催者の名前            |
| date  | Date   | 開催日時(ISO 8601 形式) |
| note  | string | 詳細など                |
| url   | string | url                     |

```javascript
{
    "id": number,
    "title": string,
    "owner": string,
    "date": Date,
    "note": string,
    "url": string
}
```

### 失敗時

#### id が存在しない時

404 NotFound

#### id と delete_key の組み合わせが合わない時

401 Unauthorized
