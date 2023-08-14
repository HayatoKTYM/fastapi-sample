API_DESC = {
    "get_user": """
  ユーザーの名前を入力し、指定可能な最大リソースを返す

  ### パスパラメータ
  - `u_id`: ユーザーID

  ### レスポンス
  - `message`: クエリ
  """,
    "ingest_log": """
  k8sから得られるユーザの利用ログをDBに追加します

  - `top`: ユーザーID CPU利用量 Memory利用量 のリスト

  ### レスポンス
  - `message`: `OK`
""",
}
