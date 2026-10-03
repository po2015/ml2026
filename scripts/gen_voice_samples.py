#!/usr/bin/env python3
"""Generate TTS sample clips for the curated voice catalog via Volcano Engine TTS.

Reads credentials from .env.volc (gitignored). Idempotent: skips voices whose
MP3 already exists in static/audio/voices/. Re-run to fill gaps after failures.
"""
import base64
import json
import os
import sys
import time
import urllib.request
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "static", "audio", "voices")
os.makedirs(OUT_DIR, exist_ok=True)

env = dict(
    l.split("=", 1)
    for l in (x.strip() for x in open(os.path.join(ROOT, ".env.volc")))
    if l and "=" in l
)
APP_ID = env["VOLC_APP_ID"].strip()
TOKEN = env["VOLC_ACCESS_TOKEN"].strip()

SAMPLE_TEXT = {
    "zh": "您好，欢迎了解 MediaLocalize 的多语言配音服务。",
    "en_us": "Welcome to MediaLocalize — your content, in every language.",
    "en_gb": "Welcome to MediaLocalize — your content, in every language.",
    "ja": "メディアローカライズへようこそ。あなたのコンテンツを世界へ。",
    "ko": "미디어로컬라이즈에 오신 것을 환영합니다.",
    "de": "Willkommen bei MediaLocalize — Ihre Inhalte, in jeder Sprache.",
    "fr": "Bienvenue chez MediaLocalize — vos contenus, dans toutes les langues.",
    "es": "Bienvenido a MediaLocalize: tu contenido, en todos los idiomas.",
    "es_mx": "Bienvenido a MediaLocalize: tu contenido, en todos los idiomas.",
    "pt_br": "Bem-vindo à MediaLocalize: seu conteúdo, em todos os idiomas.",
    "ru": "Добро пожаловать в MediaLocalize — ваш контент на любом языке.",
    "ar": "مرحبًا بكم في ميديا لوكالايز، محتواكم بكل اللغات.",
    "id": "Selamat datang di MediaLocalize — konten Anda, dalam setiap bahasa.",
    "th": "ยินดีต้อนรับสู่ MediaLocalize เนื้อหาของคุณในทุกภาษา",
    "vi": "Chào mừng đến với MediaLocalize — nội dung của bạn, bằng mọi ngôn ngữ.",
    "tl": "Maligayang pagdating sa MediaLocalize — ang inyong nilalaman, sa bawat wika.",
    "ms": "Selamat datang ke MediaLocalize — kandungan anda, dalam setiap bahasa.",
    "it": "Benvenuti in MediaLocalize: i vostri contenuti, in ogni lingua.",
}


def tts(voice: str, text: str) -> bytes:
    body = {
        "app": {"appid": APP_ID, "token": TOKEN, "cluster": "volcano_tts"},
        "user": {"uid": "medialocalize-site"},
        "audio": {"voice_type": voice, "encoding": "mp3", "speed_ratio": 1.0},
        "request": {
            "reqid": str(uuid.uuid4()),
            "text": text,
            "text_type": "plain",
            "operation": "query",
        },
    }
    req = urllib.request.Request(
        "https://openspeech.bytedance.com/api/v1/tts",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer;{TOKEN}", "Content-Type": "application/json"},
    )
    resp = json.load(urllib.request.urlopen(req, timeout=60))
    if resp.get("code") != 3000:
        raise RuntimeError(f"code={resp.get('code')} message={resp.get('message')}")
    return base64.b64decode(resp["data"])


def main() -> None:
    voices = json.load(open(os.path.join(ROOT, "data", "voices.json")))
    todo = []
    for v in voices["zh"]:
        todo.append((v["voice_type"], SAMPLE_TEXT["zh"]))
    for v in voices["foreign"]:
        todo.append((v["voice_type"], SAMPLE_TEXT[v["lang"]]))

    ok, fail = 0, []
    for i, (voice, text) in enumerate(todo, 1):
        out = os.path.join(OUT_DIR, f"{voice}.mp3")
        if os.path.exists(out) and os.path.getsize(out) > 1000:
            ok += 1
            continue
        for attempt in range(3):
            try:
                audio = tts(voice, text)
                with open(out, "wb") as f:
                    f.write(audio)
                ok += 1
                print(f"[{i}/{len(todo)}] OK {voice} ({len(audio)} B)", flush=True)
                break
            except Exception as e:  # noqa: BLE001
                print(f"[{i}/{len(todo)}] attempt {attempt+1} failed {voice}: {e}", flush=True)
                time.sleep(2 * (attempt + 1))
        else:
            fail.append(voice)
        time.sleep(0.3)

    print(f"DONE ok={ok} failed={len(fail)}", flush=True)
    for v in fail:
        print(f"FAILED {v}", flush=True)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
