# SIGNOFF A17 — авторский (стилистический) проход по PAPER_RU: остаточные человеческие решения

_Created: 11-07-2026 · Last updated: 06-09-2026_

**Paper:** [PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/PAPER_RU.md) (A17, «лексикографический хедж», RU; площадка Восток · Oriens)
**Pass:** author-voice pass per [H681](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H681-Fable_MWS_a17-lexicographic-hedge-author-pass_11.07.26.md), Fable 5 (`claude-fable-5`), 11-07-2026. Предшествующий рецензионный проход: [A17_review_fable5.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/A17_review_fable5.md) (03-07-2026, все агентно-исправимые находки закрыты, [PR #226](https://github.com/sanskrit-lexicon/MWS/pull/226)).
**Scope discipline:** ни одно число, утверждение или библиографическая ссылка не изменены; проверено пословным диффом — все числовые токены в диффе сбалансированы (удалено = восстановлено без изменений), единственный несбалансированный токен — добавленные даты правки 2026 г.

**Инструкция:** прочитать этот файл (~30 минут вместе с выборочной сверкой мест ниже), наложить вето на неудачные правки голоса (каждая обратима одним revert-редактированием), закрыть три открытых гейта §2 — после этого A17 поднимается до 5/5.

---

## 1. Правки голоса, сделанные в этом проходе (автор может наложить вето)

Каждая строка: место → что изменено → зачем. Полный дифф: PR этого прохода.

| # | Место | Было → стало | Зачем |
|---|---|---|---|
| 1 | §2, §3 (заголовок), §1 карта статьи | «грундированная модель» / «разрешающий обратный анализ (grounded analysis)» → «обоснованная (*grounded*) модель» / «логика **обоснованной теории** (*grounded theory*)» | «Обоснованная теория» — устоявшийся русский перевод Glaser & Strauss; «грундированная» — калька, «разрешающий обратный анализ» — непрозрачный неологизм |
| 2 | §1 (2×), §6.3 | «Бетлинг(а) (и Рот)» → «Бетлингк(а) и Рот(а)» | Русская индологическая норма: О. Бётлингк (без ё — Бетлингк); форма «Бетлинг» теряет финальное -к фамилии Böhtlingk; дефис между двумя лицами заменен на «и» |
| 3 | §1, §4, §6.5 | «Моньера Уильямса / Моньеру Уильямсу» → «Моньер-Уильямса / Моньер-Уильямсу» | Monier-Williams — двойная фамилия; раздельная форма читается как имя+фамилия. ⚠️ Альтернатива — традиционное «Монье-Вильямс» (как у Кочергиной): выбор формы — авторское право вето, см. §2.4 |
| 4 | Шапка, Благодарности | «реферейский проход» → «рецензионный проход» (2×) | «Реферейский» — окказионализм; регистр Востока |
| 5 | §6.5, §6.6, §7, §8 (6×) | «инлайн-» → «внутритекстовый» | Англицизм вне терминосистемы статьи; «внутритекстовая цитата/маркер» — стандартный русский термин |
| 6 | §4 | «Они и делают MW самим собой» → «Именно они определяют узнаваемый облик MW»; «набор стоит реальных денег» → «типографский набор дорог»; «уникально-MW-овская характеристика» → «уникальная особенность MW»; «изобретение Моньера Уильямса» → «личное изобретение Моньер-Уильямса» | Разговорные обороты → академический регистр |
| 7 | §6.4 | «схлопывает … в бинарную оппозицию» → «сводит … к бинарной оппозиции» (заголовок «коллапс» сохранен); «не может тащить полный аппарат … оставаться напечатаемым» → «не может нести полный аппарат …, оставаясь пригодным к изданию в одном томе» | Разговорное/неологизм → регистр; смысл не тронут |
| 8 | §6.3 | «У читателя есть путь к данным.» (отдельная ударная фраза) → слито: «— путь от пометы к первоисточнику остается открытым» | LLM-овская ударная концовка → связная фраза |
| 9 | §6.5 | Снята датировка работы «В апреле — мае 2026 г. мы прочли…» → «Мы обследовали…»; «не удалось воспроизвести через OCR в текущем проходе» → «не удалось надежно воспроизвести средствами OCR» | Лабораторный журнал → журнальный голос (прецедент A16/H079 Major 8) |
| 10 | Аннотация | «Центральная эмпирическая находка» → «Центральный эмпирический результат»; добавлена глосса «(от англ. *hedge* 'страхующая оговорка')» при первом употреблении термина | Калька «находка» (finding); термин «хедж» для русского читателя вводится глоссой |
| 11 | §6.6 | «Сила MW — в перенесении…» → «Собственный вклад MW — перенос…»; «(40 212 запросов в SQLite)» → «один запрос к SQLite-базе возвращает все 40 212 случаев» | «Сила» — разговорно; старая формула про «40 212 запросов» читалась как 40 212 *запросов*, а не 40 212 *результатов одного* запроса (число не изменено) |
| 12 | §8 (2) | «читательскую сигнализацию о «kosha-only»-свидетельстве» → «читательское предупреждение „слово засвидетельствовано только лексикографами"» | Английская вставка в русском выводе |
| 13 | §7, §8 (5) | «жанрово другие артефакты» → «артефакты иного жанра»; «Иными словами» (2-е из двух) → «Таким образом»; «на сегодня — не начата» → «пока не начата»; «самое высокоокупаемое направление» → «направление … с наибольшей ожидаемой отдачей» | Регистр, вариативность связок |
| 14 | Шапка | Добавлен ORCID [0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X) и латинская форма имени; строка версии дополнена «авторская стилистическая правка 2026-07-11» | Стандартный идентификационный блок автора |
| 15 | Благодарности | Заголовок «Отдельная благодарность» → «Благодарности»; «Marcis» → «Mārcis»; добавлена атрибуция этого прохода (Fable 5, `claude-fable-5`, 11-07-2026) | Конвенция раздела; правило атрибуции модели |
| 16 | Везде | Все внутренние относительные ссылки (PAPER.md, MICROANALYSIS.md, DOUBTS.md, analysis/, decisions/) → полные blob-URL (PAPER.md — на ветку `docs-pass`, канонический черновик A16; остальные — `master`); «*Hemachandra*» → «*Hemacandra*» (§6.4, унификация с остальным текстом) | Org-конвенция кликабельных ссылок; при подготовке DOCX для подачи ссылки конвертируются в сноски |

## 2. Открытые гейты до 5/5 (человек решает)

1. **Байлайн и аффилиация (общий гейт с A16).** В шапке — «Марцис Гасунс (Mārcis Gasūns), ORCID, gasyoun@ya.ru, от лица коллаборации CDSL». Восток требует аффилиацию — ее в шапке нет; нужно руление: независимый исследователь / иная аффилиация, и окончательная русская форма имени.
2. **ŚABDAC = Śabdacandrikā** (рецензия, m8): сверить разворот аббревиатуры с Verzeichniss PWG до печати.
3. **Фраза о параллельной подаче в обоих сопроводительных письмах** (рецензия M6): письма еще не существуют; при их создании включить disclosure-абзац.
4. **Форма «Моньер-Уильямс» vs традиционное «Монье-Вильямс»** (правка №3 выше): в русской литературе конкурируют обе; у Кочергиной — «Монье-Вильямс». Выбранная форма последовательна внутри статьи, но окончательное руление — за автором.
5. **«Беляев» в списке классиков (§6.2)**: ряд «Беляева, Зографа, Топорова, Елизаренковой» — подтвердить, какой именно Беляев имеется в виду (инициалы в тексте отсутствуют); при сомнении — снять имя или добавить инициалы.
6. **Термин «хедж»** сохранен как центральный термин статьи (в заголовке и по всему тексту) с добавленной глоссой; если для Востока англицизм в заголовке нежелателен, потребуется переименование конструкта — решение автора.

## 3. Что НЕ трогалось

Все числа, таблицы, доли, датировки данных (фиксация 2026-05-23 и пр.), библиография (состав и формы ссылок), четыре общих с A16 вывода и их маркировка «(общий / только в русской версии)», дисклозура параллельной подачи в шапке и концовке, цитаты из предисловий Каппеллера/Бенфея/MW 1872 (переводы оставлены дословно как в рецензированной версии).


---

## Pass 2 — 06-09-2026 (Fable 5.1 `claude-fable-5-1`)

**Scope.** Manuscript: [papers/microanalysis/PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/PAPER_RU.md) (A17, RU twin of A16; target Восток · Oriens). Handoff: [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md) — all-articles author-voice pass, stage 2. Model: Fable 5.1 (`claude-fable-5-1`), 06-09-2026. Voice, register and framing only; no number, claim or citation altered; mechanical drift gate ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py) against `origin/master`) CLEAN — 345 numbers, 27 URLs, 3 citations, 56 IAST tokens, 16 headings, 61 table rows count-identical before and after. Pass-1 calls (§1 above) were all found applied; this pass removes what pass 1 left: the LLM-style bold density, two «не X, а Y» punch-line clichés, empty openers, two grammar slips, calques, and the two remaining ё.

### 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Шапка, байлайн | «Марцис Гасунс (Mārcis Gasūns), ORCID …, gasyoun@ya.ru (в угловых скобках)» → «Марцис Гасунс (Mārcis Gasūns), независимый исследователь, ORCID …, gasyoun@ya.ru»; «(от лица коллаборации CDSL)» kept | Standing RU academic byline (H3857 brief); supplies the affiliation Восток requires — closes the affiliation half of pass-1 gate §2.1 (name form still open, §2.4) |
| 2 | Шапка | New line «**Проход 2:** авторский голосовой проход 2026-09-06 — Fable 5.1 (`claude-fable-5-1`), см. SIGNOFF…»; `Last updated` → 06-09-2026 | Status block lists prior passes; H3857 header-note rule. Благодарности deliberately NOT extended (brief: no note elsewhere) — see flag 4 |
| 3 | Вся проза (79 мест) | Bold stripped from mid-sentence emphasis phrases (аннотация, §1–§8, концовка). Kept: header labels, **Аннотация.**/**Ключевые слова:**, the five §3 term leads, §5 type/property names, §6.5 dictionary leads (**Каппеллер 1891** etc.), the two term-naming bolds «мы называем **блок-экономией**» (§4) and «В нашей терминологии **хедж**» (§6.1), **Благодарности.**, and every table cell | De-AI checklist «bold-every-other-word»: 107 bolds outside tables in a 5 000-word paper is a scanning aid for a reader who does not read; journal prose carries emphasis in syntax. Table cells untouched (drift gate compares rows verbatim) |
| 4 | §1, абз. 2 | «Это не вопрос изысканности или объема; это вопрос жанровой архитектуры.» → «Различие здесь не в изысканности или объеме, а в жанровой архитектуре.» | Two-clause «It's not X, it's Y» cliché |
| 5 | §1, абз. 3 | «Последнее — особенно значимо: Каппеллер был соредактором MW 1899.» → «Последнее обстоятельство существенно: …» | Filler intensifier on a dash fragment |
| 6 | §1, карта статьи | «§8 — выводы для современной индологии …» → «В §8 подводятся выводы …» | Telegram syntax (dropped verb) in a sentence whose neighbours all carry verbs |
| 7 | §4 | «в ~4 раза плотнее цитированиями» → «плотнее по цитированию» | Case government |
| 8 | §4, посл. абз. | «Существенно, что кросс-словарный аудит показывает: сама форма …» → «Кросс-словарный аудит показывает при этом, что сама форма …» | Empty opener («importantly»); claim, hedging unchanged |
| 9 | §5 | «Остаточная «прочее» после этого сжимается» → «Остаточная категория «прочее» …» | Gender agreement (остаточная / прочее) |
| 10 | §6.1 | «блок, чья функция в том, чтобы модифицировать» → «блок, функция которого — модифицировать» | «чья» with an inanimate head reads colloquial; shorter |
| 11 | §6.1 (а) | «на уровне статьи целиком, не уровне слота» → «…, а не на уровне слота» | Dropped preposition |
| 12 | §6.3 | «генерический хедж *L.* отсутствует — ноль раз.» → «… не встречается ни разу.» | Dash-plus-bold punch line; the count (zero) is unchanged |
| 13 | §6.4 | «Но *L.* — не только компромисс. Это и типологически значимая декларация:» → one sentence «…, но и типологически значимая декларация:» | Parcellation for effect |
| 14 | §6.5, абз. 1 | «трех англо-санскритских словарей» → «трех санскритско-английских словарей» | **Reverted after adversarial verify:** direction descriptor is substance, not voice — original «англо-санскритских» restored; flagged in §2 below for a human |
| 15 | §6.5, Каппеллер | «точный аналог MW-овского `<ls>L.</ls>`» → «точный аналог хеджа MW `<ls>L.</ls>`» | «MW-овский» colloquial (pass 1 already removed its twin in §4) |
| 16 | §6.5, Бенфей | «Тип интервенции тождествен; семантическая нагрузка различна.» → «Тип приема тождествен, семантическая нагрузка различна.» | «интервенция» is a calque of *intervention* |
| 17 | §6.5, Уилсон | «трактуем Уилсона как «без явной конвенции хеджа, основанной только на печатных источниках»» → «трактуем Уилсона как словарь без явной конвенции хеджа, опирающийся только на печатные источники» | **Reverted after adversarial verify:** the quoted string is the classification label itself; unquoting it changed the meaning — original wording restored verbatim |
| 18 | §6.6 | «`<ls>L.</ls>` **есть** цитата» → «*есть* цитата» | Copula emphasis in italics, not bold |
| 19 | §6.6 | «Дополнительный нюанс: соредактором MW был Каппеллер.» → «К этому добавляется уже отмеченное обстоятельство: соредактором MW был Каппеллер.» | «нюанс» (de-AI list) and the fact is stated for the third time — the new wording admits the repetition instead of dressing it as new |
| 20 | §6.6, посл. абз. | «Это значительно более интересная картина, чем простая «MW изобрел всё» или «MW позаимствовал всё».» → «Эта картина сложнее, чем простое «MW изобрел все» или «MW позаимствовал все».» | Self-praise («значительно более интересная»); removes the paper's last two ё (see flag 6) |
| 21 | §7, посл. абз. | «Это, вообще говоря, не критика *kośa* — это констатация того, что они — другой жанр, …» → «Это не критика *kośa*, а констатация того, что они принадлежат другому жанру, …» | **Partially reverted after adversarial verify:** «вообще говоря» is a hedge, not filler — restored; the de-dashed «не X, а Y» form kept |
| 22 | §8 (4) | «дизайнерские контрасты» → «контрасты в устройстве словарей» | Calque of *design contrasts* |
| 23 | Не сделано | Авторское «мы» kept throughout (Восток norm; the byline speaks «от лица коллаборации CDSL»); all 16 headings untouched, including the rhetorical «6.5 Кто это начал?»; «MW1899» (§3 ×2, §4) vs «MW 1899» elsewhere left as is | First-person singular would misstate a collaboration paper; heading wording and the MW1899 spacing are mechanical and better ruled by the author in one sweep |

### 2. Substance flags carried (not fixed)

1. **§6.6 «Сопоставление трех предшественников»** — the table that follows holds two predecessors (Каппеллер 1891, Бенфей 1866) and MW 1899 itself; «трех» is a count word and was left. Suggested: «Сопоставление MW с двумя предшественниками».
2. **Cappeller-as-co-editor stated three times** (§1 abstract-level, §6.5, §6.6) — repetition is now acknowledged in §6.6 (call 19) but not cut; a human may drop one instance.
3. **PAPER.md links point at branch `docs-pass`** (8 links; the branch still exists on origin at `530774f`). If the EN twin lands on `master`, all eight go stale — URLs are substance for the drift gate, so untouched.
4. **Благодарности** name the 03-07 review and the 11-07 pass but not this one; the H3857 brief forbids adding the note anywhere but the status block, so attribution for pass 2 lives in the new «Проход 2» header line only. A human may mirror it into Благодарности before submission.
5. **Carried from pass 1 §2** (all still open): ŚABDAC = Śabdacandrikā against PWG's Verzeichniss (§2.2); «Моньер-Уильямс» vs «Монье-Вильямс» (§2.4); which Беляев in §6.2 (§2.5); «хедж» as a title term (§2.6); dual-submission disclosure sentence in both cover letters (§2.3).
6. **ё policy conflict.** [PR #239 / H543](https://github.com/sanskrit-lexicon/MWS/pull/239) dropped ё «keeping the всё/все distinction»; the H3857 brief says Russian text never uses ё. This pass followed the brief (the two «всё» in §6.6 were unambiguous in context); a human should decide which rule governs the submitted DOCX.
7. **Submission freeze** until 2026-11-01 stands; nothing here is a submission CTA.
8. **§6.5 direction descriptor looks wrong** — «трех англо-санскритских словарей» names English→Sanskrit, while Wilson 1832, Benfey 1866 and Cappeller 1891 are Sanskrit→English by their own titles. Restored to the original after the pass-2 change was refuted as a substance edit; a human should decide whether to change it to «санскритско-английских».

### 3. Read-and-sign

About 30 minutes: read §1–§2 of this Pass 2 block, spot-check calls 3, 14, 19 and 20 in the manuscript, veto by reverting the single hunk. Proposed readiness after vetoes and pass-1 gates §2.2/§2.4/§2.5: 5/5 — proposal only, the human sets it. Venue: Восток · Oriens stands; no change recommended.

_Dr. Mārcis Gasūns_
