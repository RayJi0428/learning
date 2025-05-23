# SetTimeout v.s. RequestAnimationFrame


| 項目     | `setTimeout`                         | `requestAnimationFrame`                           |
| -------- | ------------------------------------ | ------------------------------------------------- |
| 調用頻率 | 依照你設定的毫秒值（不一定準確）     | 約每秒 60 次（與螢幕刷新率同步）                  |
| 精準度   | 低，可能延遲或提早                   | 高，系統會自動同步畫面時間                        |
| 執行時機 | 排入事件佇列中執行，可能與渲染錯開   | **在下一幀畫面刷新前執行**                        |
| 適合用途 | 一般非同步任務、延遲執行、輪詢等     | **動畫、畫面更新、遊戲畫面刷新**                  |
| 是否節能 | 否，即使頁面未顯示仍會持續執行       | ✅ 背景分頁會自動暫停，不佔資源                    |
| 回傳值   | timeout ID，可用 `clearTimeout` 取消 | 回傳 request ID，可用 `cancelAnimationFrame` 取消 |


| 行為                   | `setTimeout` 可能的結果 |
| ---------------------- | ----------------------- |
| 背景分頁               | 延遲到 1 秒以上         |
| `alert()` / 長同步任務 | 延遲直到主線程釋放      |
| CPU 忙碌或渲染阻塞     | 無限延後                |
| 睡眠 / 鎖定電腦        | 完全卡住直到醒來才執行  |
| 被取消 / 覆蓋變數      | 完全不執行              |
| 被 CSP 沙盒環境限制    | 被封鎖或行為異常        |
