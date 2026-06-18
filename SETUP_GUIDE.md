# Quiz Master — Simple Steps to Get a Play-Store-Ready APK

You're phone-only with no computer, so everything below runs in GitHub's
free cloud build servers, controlled entirely from your phone's browser.
The only step that wants a real computer is the very first upload — and
even that can be borrowed (library, friend, school) for 10 minutes.

## What's already done for you
- The full app (Kotlin/Android Studio project)
- AdMob App ID and interstitial ad unit — both your real ones
- A real release signing key, already generated (see "Files I'm giving
  you" below) — this is what turns an unsigned build into one Play Store
  will actually accept
- A cloud build pipeline (GitHub Actions) that produces both a debug APK
  (to test/play right now) and a signed release AAB (to upload to Play
  Store) automatically
- A privacy policy page, ready to host for free

## Files I'm giving you
1. **QuizMaster.zip** — the project. Upload this to GitHub.
2. **quizmaster-release.keystore** — your signing key. **Never put this in
   GitHub or anywhere public.** It only goes into a GitHub Secret (step 3
   below), which GitHub keeps encrypted and never displays again once saved.
3. **KEYSTORE_CREDENTIALS.txt** — the password and other values you'll
   paste into GitHub Secrets. Save this somewhere private (password
   manager, notes app) — if you lose this password along with the
   keystore, you can never update this app again under the same listing,
   ever, and would have to publish as a brand new app.

---

## Step 1 — Get the project onto GitHub (needs any computer, ~10 min)

1. On any computer's browser: go to [github.com](https://github.com) →
   sign up (free).
2. **New repository** → name it `quiz-master` → choose **Private** (keeps
   your code out of public view) → Create.
3. **Add file → Upload files** → unzip `QuizMaster.zip` first, then drag
   the whole unzipped `QuizMaster` folder onto the page → **Commit changes**.

## Step 2 — Add your signing key as GitHub Secrets (from your phone)

This lets the cloud build sign the release file with your real key,
without your key ever being stored in the repo itself.

1. On your phone, open your repo → **Settings** tab → **Secrets and
   variables → Actions** → **New repository secret**.
2. Create three secrets (open `KEYSTORE_CREDENTIALS.txt` for the exact
   values to paste):
   - `KEYSTORE_BASE64` → paste the long text block from that file
   - `KEYSTORE_PASSWORD` → paste the password
   - `KEY_ALIAS` → paste the alias (`quizmaster`)

## Step 3 — Build it (from your phone)

1. Go to the **Actions** tab in your repo.
2. A build should already be running from your Step 1 upload. If not, tap
   **Build Quiz Master APK → Run workflow**.
3. Wait 3-8 minutes, tap into the finished run, scroll to **Artifacts**.
4. Download **QuizMaster-debug-apk** → unzip on your phone → tap the
   `.apk` → install (allow "install unknown apps" if asked) → **play it**.
5. Download **QuizMaster-release-aab** — this is the signed file for Play
   Store. Keep it; you'll upload it in Step 5.

If the AAB artifact is missing, your secrets from Step 2 likely aren't set
correctly yet — double check the three values match `KEYSTORE_CREDENTIALS.txt`
exactly, then re-run the workflow.

## Step 4 — Host your privacy policy (free, from your phone)

Play Store requires a privacy policy URL since this app shows ads.

1. In your repo → **Settings → Pages**.
2. Under "Build and deployment", source: **Deploy from a branch** →
   branch: **main**, folder: **/ (root)** → **Save**.
3. Wait a minute, then your policy is live at:
   `https://YOUR-USERNAME.github.io/quiz-master/privacy_policy.html`
4. Before that works well, edit `privacy_policy.html` in your repo (tap the
   file → pencil/edit icon) and replace `REPLACE_WITH_YOUR_EMAIL@example.com`
   with your real contact email.

## Step 5 — Publish on Google Play

1. Create a [Google Play Console](https://play.google.com/console) account
   ($25 one-time fee).
2. **Create app** → fill in name, language, app/game type, free.
3. Fill in the required sections in the left menu (Play Console walks you
   through each, all doable from a phone browser):
   - **Store listing**: short/full description, app icon, at least 2
     screenshots (play the debug APK and take screenshots on your phone)
   - **Privacy policy**: paste your GitHub Pages URL from Step 4
   - **App content**: content rating questionnaire, target audience
     (declare ads, since AdMob is in use), Data Safety form (declare:
     email collected locally for accounts, advertising data via AdMob —
     see `privacy_policy.html` for exact wording to reuse)
4. **Production → Create new release** → upload the **AAB file** from
   Step 3 → fill in release notes → save → review → roll out.

Google typically reviews new apps within a few hours to a few days.

---

## Things still worth doing before launch

- **Banner ad unit**: still using Google's test ID. Create a real Banner
  ad unit in AdMob console and replace `TEST_BANNER_UNIT_ID` in
  `MainActivity.kt` (then re-upload that one changed file to GitHub and
  re-run the build).
- **Redeem contact info**: `RedeemActivity.kt` still has placeholder
  `OWNER_EMAIL` / `OWNER_WHATSAPP_NUMBER` — set these to where you actually
  want redeem requests sent.
- **Decide what the redeem code is worth**: a fun in-app badge needs no
  more setup; a real prize means you must actually honor the 24-hour
  promise the app makes to players.
- **Spot-check the question bank** (`app/src/main/assets/questions.json`)
  — it was generated programmatically from general knowledge, not pulled
  from a verified source.
- **The admin password** (`19202175`) is a string compiled into the app —
  anyone who decompiles the APK can read it. Fine as a casual gate, not
  real security.
