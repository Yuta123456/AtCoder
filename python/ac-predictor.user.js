/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 9);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

module.exports = jQuery;

/***/ }),
/* 1 */
/***/ (function(module, exports) {

module.exports = usLibs.rating;

/***/ }),
/* 2 */
/***/ (function(module, exports) {

module.exports = usLibs.global;

/***/ }),
/* 3 */
/***/ (function(module, exports) {

module.exports = usLibs.data;

/***/ }),
/* 4 */
/***/ (function(module, exports) {

module.exports = sidemenu;

/***/ }),
/* 5 */
/***/ (function(module, exports) {

module.exports = moment;

/***/ }),
/* 6 */
/***/ (function(module, exports) {

module.exports = "<div id=\"predictor-alert\" class=\"row\"><h5 class='sidemenu-txt'>読み込み中…</h5></div>\r\n<div id=\"predictor-data\" class=\"row\">\r\n    <div class=\"input-group col-xs-12\">\r\n        <span class=\"input-group-addon\">順位<span class=\"glyphicon glyphicon-question-sign\" aria-hidden=\"true\" data-html=\"true\" data-toggle=\"tooltip\" data-placement=\"right\" title=\"\" data-original-title=\"Rated内の順位です。複数人同順位の際は人数を加味します(5位が4人居たら6.5位として計算)\"></span></span>\r\n        <input class=\"form-control\" id=\"predictor-input-rank\">\r\n        <span class=\"input-group-addon\">位</span>\r\n    </div>\r\n        \r\n    <div class=\"input-group col-xs-12\">\r\n        <span class=\"input-group-addon\">パフォーマンス</span>\r\n        <input class=\"form-control\" id=\"predictor-input-perf\">\r\n    </div>\r\n\r\n    <div class=\"input-group col-xs-12\">\r\n        <span class=\"input-group-addon\">レーティング</span>\r\n        <input class=\"form-control\" id=\"predictor-input-rate\">\r\n    </div>\r\n</div>\r\n<div class=\"row\">\r\n    <div class=\"btn-group\">\r\n        <button class=\"btn btn-default\" id=\"predictor-current\">現在の順位</button>\r\n        <button type=\"button\" class=\"btn btn-primary\" id=\"predictor-reload\" data-loading-text=\"更新中…\">更新</button>\r\n        <!--<button class=\"btn btn-default\" id=\"predictor-solved\" disabled>現問題AC後</button>-->\r\n    </div>\r\n</div>";

/***/ }),
/* 7 */
/***/ (function(module, exports) {

module.exports = usLibs.contestInformation;

/***/ }),
/* 8 */
/***/ (function(module, exports) {

module.exports = "<div id=\"estimator-alert\"></div>\r\n<div class=\"row\">\r\n\t<div class=\"input-group\">\r\n\t\t<span class=\"input-group-addon\" id=\"estimator-input-desc\"></span>\r\n\t\t<input type=\"number\" class=\"form-control\" id=\"estimator-input\">\r\n\t</div>\r\n</div>\r\n<div class=\"row\">\r\n\t<div class=\"input-group\">\r\n\t\t<span class=\"input-group-addon\" id=\"estimator-res-desc\"></span>\r\n\t\t<input class=\"form-control\" id=\"estimator-res\" disabled=\"disabled\">\r\n\t\t<span class=\"input-group-btn\">\r\n\t\t\t<button class=\"btn btn-default\" id=\"estimator-toggle\">入替</button>\r\n\t\t</span>\r\n\t</div>\r\n</div>\r\n<div class=\"row\" style=\"margin: 10px 0px;\">\r\n\t<a class=\"btn btn-default col-xs-offset-8 col-xs-4\" rel=\"nofollow\" onClick=\"window.open(encodeURI(decodeURI(this.href)),'twwindow','width=550, height=450, personalbar=0, toolbar=0, scrollbars=1'); return false;\" id='estimator-tweet'>ツイート</a>\r\n</div>";

/***/ }),
/* 9 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);

// EXTERNAL MODULE: external "sidemenu"
var external_sidemenu_ = __webpack_require__(4);

// EXTERNAL MODULE: external "jQuery"
var external_jQuery_ = __webpack_require__(0);

// EXTERNAL MODULE: ./src/elements/predictor/dom.html
var dom = __webpack_require__(6);
var dom_default = /*#__PURE__*/__webpack_require__.n(dom);

// EXTERNAL MODULE: external "moment"
var external_moment_ = __webpack_require__(5);
var external_moment_default = /*#__PURE__*/__webpack_require__.n(external_moment_);

// CONCATENATED MODULE: ./src/libs/contest/results/result.js
class Result {
    /***
     * @param {boolean} isRated
     * @param {boolean} isSubmitted
     * @param {string} userScreenName
     * @param {number} performance
     * @param {number} place
     * @param {number} ratedRank
     * @param {number} competitions
     * @param {number} innerPerformance
     * @param {number} oldRating
     * @param {number} newRating
     */
    constructor(
        isRated,
        isSubmitted,
        userScreenName,
        place,
        ratedRank,
        oldRating,
        newRating,
        competitions,
        performance,
        innerPerformance
    ) {
        this.IsRated = isRated;
        this.IsSubmitted = isSubmitted;
        this.UserScreenName = userScreenName;
        this.Place = place;
        this.RatedRank = ratedRank;
        this.OldRating = oldRating;
        this.NewRating = newRating;
        this.Competitions = competitions;
        this.Performance = performance;
        this.InnerPerformance = innerPerformance;
    }
}

// CONCATENATED MODULE: ./src/libs/contest/contest.js


class contest_Contest {
    constructor(contestScreenName, contestInformation, standings, aPerfs) {
        this.ratedLimit = contestInformation.RatedRange[1] + 1;
        this.perfLimit = this.ratedLimit + 400;
        this.standings = standings;
        this.aPerfs = aPerfs;
        this.rankMemo = {};

        const analyzedData = analyzeStandingsData(
            standings.Fixed,
            standings.StandingsData,
            aPerfs,
            { 2000: 800, 2800: 1000, Infinity: 1200 }[this.ratedLimit] || 1200,
            this.ratedLimit
        );
        this.contestantAPerf = analyzedData.contestantAPerf;
        this.templateResults = analyzedData.templateResults;
        this.IsRated = analyzedData.isRated;

        /** @return {{contestantAPerf: number[], templateResults: Object<string, Result>, isRated: boolean}} */
        function analyzeStandingsData(
            fixed,
            standingsData,
            aPerfs,
            defaultAPerf,
            ratedLimit
        ) {
            let analyzedData = analyze(
                data => data.IsRated && data.TotalResult.Count !== 0
            );
            analyzedData.isRated = true;
            if (analyzedData.contestantAPerf.length === 0) {
                analyzedData = analyze(
                    data =>
                        data.OldRating < ratedLimit &&
                        data.TotalResult.Count !== 0
                );
                analyzedData.isRated = false;
            }
            return analyzedData;

            /** @return {{contestantAPerf: number[], templateResults: Object.<string, Result>}}*/
            function analyze(isUserRated) {
                let contestantAPerf = [];
                let templateResults = {};

                let currentRatedRank = 1;

                let lastRank = 0;
                let tiedUsers = [];
                let ratedInTiedUsers = 0;
                function applyTiedUsers() {
                    tiedUsers.forEach(data => {
                        if (isUserRated(data)) {
                            contestantAPerf.push(
                                aPerfs[data.UserScreenName] || defaultAPerf
                            );
                            ratedInTiedUsers++;
                        }
                    });

                    let ratedRank =
                        currentRatedRank +
                        Math.max(0, ratedInTiedUsers - 1) / 2;
                    tiedUsers.forEach(data => {
                        templateResults[data.UserScreenName] = new Result(
                            isUserRated(data),
                            data.TotalResult.Count !== 0,
                            data.UserScreenName,
                            data.Rank,
                            ratedRank,
                            fixed ? data.OldRating : data.Rating,
                            null,
                            data.Competitions,
                            null,
                            null
                        );
                    });
                    currentRatedRank += ratedInTiedUsers;
                    tiedUsers.length = 0;
                    ratedInTiedUsers = 0;
                }

                standingsData.forEach(data => {
                    if (lastRank !== data.Rank) applyTiedUsers();
                    lastRank = data.Rank;
                    tiedUsers.push(data);
                });
                applyTiedUsers();

                return {
                    contestantAPerf: contestantAPerf,
                    templateResults: templateResults
                };
            }
        }
    }

    getRatedRank(X) {
        if (this.rankMemo[X]) return this.rankMemo[X];
        return (this.rankMemo[X] = this.contestantAPerf.reduce(
            (val, APerf) =>
                val + 1.0 / (1.0 + Math.pow(6.0, (X - APerf) / 400.0)),
            0
        ));
    }

    getPerf(ratedRank) {
        return Math.min(this.getInnerPerf(ratedRank), this.perfLimit);
    }

    getInnerPerf(ratedRank) {
        let upper = 6144;
        let lower = -2048;
        while (upper - lower > 0.5) {
            const mid = (upper + lower) / 2;
            if (ratedRank - 0.5 > this.getRatedRank(mid)) upper = mid;
            else lower = mid;
        }
        return Math.round((upper + lower) / 2);
    }
}

// CONCATENATED MODULE: ./src/libs/contest/results/results.js
class Results {
    constructor() {}
    /**
     * @param {string} userScreenName
     * @return {Result}
     */
    getUserResult(userScreenName) {}
}

// EXTERNAL MODULE: external "usLibs.rating"
var external_usLibs_rating_ = __webpack_require__(1);

// CONCATENATED MODULE: ./src/libs/contest/results/standingsResults.js



class standingsResults_OnDemandResults extends Results {
    /**
     * @param {Contest} contest
     * @param {Results[]} templateResults
     */
    constructor(contest, templateResults) {
        super();
        this.Contest = contest;
        this.TemplateResults = templateResults;
    }
    /**
     * @param {string} userScreenName
     * @return {Result}
     */
    getUserResult(userScreenName) {
        const baseResults = this.TemplateResults[userScreenName];
        if (!baseResults) return null;
        if (!baseResults.Performance) {
            baseResults.InnerPerformance = this.Contest.getInnerPerf(
                baseResults.RatedRank
            );
            baseResults.Performance = Math.min(
                baseResults.InnerPerformance,
                this.Contest.perfLimit
            );
            baseResults.NewRating = Math.round(
                Object(external_usLibs_rating_["positivizeRating"])(
                    Object(external_usLibs_rating_["calcRatingFromLast"])(
                        Object(external_usLibs_rating_["unpositivizeRating"])(baseResults.OldRating),
                        baseResults.Performance,
                        baseResults.Competitions
                    )
                )
            );
        }
        return baseResults;
    }
}

// CONCATENATED MODULE: ./src/libs/contest/results/fIxedResults.js


class fIxedResults_FixedResults extends Results {
    /**
     * @param {Result[]} results
     */
    constructor(results) {
        super();
        this.resultsDic = {};
        results.forEach(result => {
            this.resultsDic[result.UserScreenName] = result;
        });
    }
    /**
     * @param {string} userScreenName
     * @return {Result}
     */
    getUserResult(userScreenName) {
        return this.resultsDic[userScreenName] || null;
    }
}

// CONCATENATED MODULE: ./src/elements/predictor/model/PredictorModel.js
class PredictorModel {
    /**
     * @param {PredictorModel} [model]
     */
    constructor(model) {
        this.enabled = model.enabled;
        this.contest = model.contest;
        this.history = model.history;
        this.updateInformation(model.information);
        this.updateData(model.rankValue, model.perfValue, model.rateValue);
    }

    /**
     * @param {boolean} state
     */
    setEnable(state) {
        this.enabled = state;
    }

    /**
     * @param {string} information
     */
    updateInformation(information) {
        this.information = information;
    }

    /**
     * @param {number} rankValue
     * @param {number} perfValue
     * @param {number} rateValue
     */
    updateData(rankValue, perfValue, rateValue) {
        this.rankValue = rankValue;
        this.perfValue = perfValue;
        this.rateValue = rateValue;
    }
}

// CONCATENATED MODULE: ./src/elements/predictor/model/calcFromRankModel.js



class calcFromRankModel_CalcFromRankModel extends PredictorModel {
    updateData(rankValue, perfValue, rateValue) {
        perfValue = this.contest.getPerf(rankValue);
        rateValue = Object(external_usLibs_rating_["positivizeRating"])(
            Object(external_usLibs_rating_["calcRatingFromHistory"])([perfValue].concat(this.history))
        );
        super.updateData(rankValue, perfValue, rateValue);
    }
}

// CONCATENATED MODULE: ./src/elements/predictor/model/calcFromPerfModel.js



class calcFromPerfModel_CalcFromPerfModel extends PredictorModel {
    updateData(rankValue, perfValue, rateValue) {
        rankValue = this.contest.getRatedRank(perfValue);
        rateValue = Object(external_usLibs_rating_["positivizeRating"])(
            Object(external_usLibs_rating_["calcRatingFromHistory"])([perfValue].concat(this.history))
        );
        super.updateData(rankValue, perfValue, rateValue);
    }
}

// CONCATENATED MODULE: ./src/elements/predictor/model/calcFromRateModel.js



class calcFromRateModel_CalcFromRateModel extends PredictorModel {
    updateData(rankValue, perfValue, rateValue) {
        perfValue = Object(external_usLibs_rating_["calcRequiredPerformance"])(
            Object(external_usLibs_rating_["unpositivizeRating"])(rateValue),
            this.history
        );
        rankValue = this.contest.getRatedRank(perfValue);
        super.updateData(rankValue, perfValue, rateValue);
    }
}

// CONCATENATED MODULE: ./src/libs/utils/roundValue.js
function roundValue(value, digit) {
    return Math.round(value * 10 ** digit) / 10 ** digit;
}

// EXTERNAL MODULE: external "usLibs.data"
var external_usLibs_data_ = __webpack_require__(3);

// EXTERNAL MODULE: external "usLibs.global"
var external_usLibs_global_ = __webpack_require__(2);

// EXTERNAL MODULE: external "usLibs.contestInformation"
var external_usLibs_contestInformation_ = __webpack_require__(7);

// CONCATENATED MODULE: ./src/elements/predictor/script.js


















let predictor = new external_sidemenu_["SideMenuElement"](
    "predictor",
    "Predictor",
    /atcoder.jp\/contests\/.+/,
    dom_default.a,
    afterAppend
);

const firstContestDate = external_moment_default()("2016-07-16 21:00");
const predictorElements = [
    "predictor-input-rank",
    "predictor-input-perf",
    "predictor-input-rate",
    "predictor-current",
    "predictor-reload",
    "predictor-tweet"
];

async function afterAppend() {
    const isStandingsPage = /standings([^/]*)?$/.test(document.location.href);
    const contestInformation = await Object(external_usLibs_contestInformation_["fetchContestInformation"])(external_usLibs_global_["contestScreenName"]);

    /** @type Results */
    let results;

    /** @type Contest */
    let contest;

    /** @type PredictorModel */
    let model = new PredictorModel({
        rankValue: 0,
        perfValue: 0,
        rateValue: 0,
        enabled: false,
        history: Object(external_usLibs_data_["getPerformanceHistories"])(await Object(external_usLibs_data_["getMyHistoryData"])())
    });

    try {
      external_jQuery_('[data-toggle="tooltip"]').tooltip();
    }
    catch (e) {  }

    if (!shouldEnabledPredictor().verdict) {
        model.updateInformation(shouldEnabledPredictor().message);
        updateView();
        return;
    }

    try {
        await initPredictor();
    } catch (e) {
        model.updateInformation(e.message);
        model.setEnable(false);
        updateView();
    }

    subscribeEvents();

    function subscribeEvents() {
        external_jQuery_("#predictor-reload").click(async () => {
            model.updateInformation("読み込み中…");
            external_jQuery_("#predictor-reload").button("loading");
            updateView();
            await updateStandingsFromAPI();
            external_jQuery_("#predictor-reload").button("reset");
            updateView();
        });
        external_jQuery_("#predictor-current").click(function() {
            const myResult = contest.templateResults[external_usLibs_global_["userScreenName"]];
            if (!myResult) return;
            model = new calcFromRankModel_CalcFromRankModel(model);
            model.updateData(
                myResult.RatedRank,
                model.perfValue,
                model.rateValue
            );
            updateView();
        });
        external_jQuery_("#predictor-input-rank").keyup(function() {
            const inputString = external_jQuery_("#predictor-input-rank").val();
            if (!isFinite(inputString)) return;
            const inputNumber = parseInt(inputString);
            model = new calcFromRankModel_CalcFromRankModel(model);
            model.updateData(inputNumber, 0, 0);
            updateView();
        });
        external_jQuery_("#predictor-input-perf").keyup(function() {
            const inputString = external_jQuery_("#predictor-input-perf").val();
            if (!isFinite(inputString)) return;
            const inputNumber = parseInt(inputString);
            model = new calcFromPerfModel_CalcFromPerfModel(model);
            model.updateData(0, inputNumber, 0);
            updateView();
        });
        external_jQuery_("#predictor-input-rate").keyup(function() {
            const inputString = external_jQuery_("#predictor-input-rate").val();
            if (!isFinite(inputString)) return;
            const inputNumber = parseInt(inputString);
            model = new calcFromRateModel_CalcFromRateModel(model);
            model.updateData(0, 0, inputNumber);
            updateView();
        });
    }

    async function initPredictor() {
        let aPerfs;
        let standings;

        try {
            standings = await Object(external_usLibs_data_["getStandingsData"])(external_usLibs_global_["contestScreenName"]);
        } catch (e) {
            throw new Error("順位表の取得に失敗しました。");
        }

        try {
            aPerfs = await getAPerfsFromAPI();
        } catch (e) {
            throw new Error("APerfの取得に失敗しました。");
        }

        async function getAPerfsFromAPI() {
            return await Object(external_usLibs_data_["getAPerfsData"])(external_usLibs_global_["contestScreenName"]);
        }

        await updateData(aPerfs, standings);
        model.setEnable(true);
        model.updateInformation(`最終更新 : ${external_moment_default()().format("HH:mm:ss")}`);

        if (isStandingsPage) {
            external_jQuery_("thead > tr").append(
                '<th class="standings-result-th" style="width:84px;min-width:84px;">perf</th><th class="standings-result-th" style="width:168px;min-width:168px;">レート変化</th>'
            );
            new MutationObserver(addPerfToStandings).observe(
                document.getElementById("standings-tbody"),
                { childList: true }
            );
            let refreshElem = document.getElementById("refresh");
            if (refreshElem)
                new MutationObserver(async mutationRecord => {
                    const isDisabled = mutationRecord[0].target.classList.contains(
                        "disabled"
                    );
                    if (isDisabled) {
                        await updateStandingsFromAPI();
                        updateView();
                    }
                }).observe(refreshElem, {
                    attributes: true,
                    attributeFilter: ["class"]
                });
        }
        updateView();
    }

    async function updateStandingsFromAPI() {
        try {
            const shouldEnabled = shouldEnabledPredictor();
            if (!shouldEnabled.verdict) throw new Error(shouldEnabled.message);
            const standings = await Object(external_usLibs_data_["getStandingsData"])(external_usLibs_global_["contestScreenName"]);
            await updateData(contest.aPerfs, standings);
            model.updateInformation(
                `最終更新 : ${external_moment_default()().format("HH:mm:ss")}`
            );
            model.setEnable(true);
        } catch (e) {
            model.updateInformation(e.message);
            model.setEnable(false);
        }
    }

    async function updateData(aperfs, standings) {
        if (Object.keys(aperfs).length === 0) {
            throw new Error("APerfのデータが提供されていません");
        }
        contest = new contest_Contest(
            external_usLibs_global_["contestScreenName"],
            contestInformation,
            standings,
            aperfs
        );
        model.contest = contest;
        await updateResultsData();
    }

    function updateView() {
        const roundedRankValue = isFinite(model.rankValue)
            ? roundValue(model.rankValue, 2)
            : "";
        const roundedPerfValue = isFinite(model.perfValue)
            ? roundValue(model.perfValue, 2)
            : "";
        const roundedRateValue = isFinite(model.rateValue)
            ? roundValue(model.rateValue, 2)
            : "";
        external_jQuery_("#predictor-input-rank").val(roundedRankValue);
        external_jQuery_("#predictor-input-perf").val(roundedPerfValue);
        external_jQuery_("#predictor-input-rate").val(roundedRateValue);

        external_jQuery_("#predictor-alert").html(
            `<h5 class='sidemenu-txt'>${model.information}</h5>`
        );

        if (model.enabled) enabled();
        else disabled();

        if (isStandingsPage) {
            addPerfToStandings();
        }
        function enabled() {
            external_jQuery_("#predictor-reload").button("reset");
            predictorElements.forEach(element => {
                external_jQuery_(`#${element}`).removeAttr("disabled");
            });
        }
        function disabled() {
            external_jQuery_("#predictor-reload").button("reset");
            predictorElements.forEach(element => {
                external_jQuery_(`#${element}`).attr("disabled", true);
            });
        }
    }

    function shouldEnabledPredictor() {
        if (!external_usLibs_global_["startTime"].isBefore())
            return { verdict: false, message: "コンテストは始まっていません" };
        if (external_moment_default()(external_usLibs_global_["startTime"]) < firstContestDate)
            return {
                verdict: false,
                message: "現行レートシステム以前のコンテストです"
            };
        if (contestInformation.RatedRange[0] > contestInformation.RatedRange[1])
            return {
                verdict: false,
                message: "ratedなコンテストではありません"
            };
        return { verdict: true, message: "" };
    }

    //全員の結果データを更新する
    async function updateResultsData() {
        if (contest.standings.Fixed && contest.IsRated) {
            let rawResult = await Object(external_usLibs_data_["getResultsData"])(external_usLibs_global_["contestScreenName"]);
            rawResult.sort((a, b) =>
                a.Place !== b.Place
                    ? a.Place - b.Place
                    : b.OldRating - a.OldRating
            );
            let sortedStandingsData = Array.from(
                contest.standings.StandingsData
            ).filter(x => x.TotalResult.Count !== 0);
            sortedStandingsData.sort((a, b) =>
                a.TotalResult.Count === 0 && b.TotalResult.Count === 0
                    ? 0
                    : a.TotalResult.Count === 0
                    ? 1
                    : b.TotalResult.Count === 0
                    ? -1
                    : a.Rank !== b.Rank
                    ? a.Rank - b.Rank
                    : b.OldRating !== a.OldRating
                    ? b.OldRating - a.OldRating
                    : a.UserIsDeleted
                    ? -1
                    : b.UserIsDeleted
                    ? 1
                    : 0
            );

            let lastPerformance = contest.perfLimit;
            let deletedCount = 0;
            results = new fIxedResults_FixedResults(
                sortedStandingsData.map((data, index) => {
                    let result = rawResult[index - deletedCount];
                    if (!result || data.OldRating !== result.OldRating) {
                        deletedCount++;
                        result = null;
                    }
                    return new Result(
                        result ? result.IsRated : false,
                        data.TotalResult.Count !== 0,
                        data.UserScreenName,
                        data.Rank,
                        -1,
                        data.OldRating,
                        result ? result.NewRating : 0,
                        0,
                        result && result.IsRated
                            ? (lastPerformance = result.Performance)
                            : lastPerformance,
                        result ? result.InnerPerformance : 0
                    );
                })
            );
        } else {
            results = new standingsResults_OnDemandResults(contest, contest.templateResults);
        }
    }

    //結果データを順位表に追加する
    function addPerfToStandings() {
        external_jQuery_(".standings-perf , .standings-rate").remove();

        external_jQuery_("#standings-tbody > tr").each((index, elem) => {
            if (elem.firstElementChild.textContent === "-") {
                let longCell = elem.getElementsByClassName(
                    "standings-result"
                )[0];
                longCell.setAttribute(
                    "colspan",
                    parseInt(longCell.getAttribute("colspan")) + 2
                );
                return;
            }
            const result = results
                ? results.getUserResult(
                      external_jQuery_(".standings-username .username span", elem).text()
                  )
                : null;
            const perfElem =
                !result || !result.IsSubmitted
                    ? "-"
                    : getRatingSpan(Math.round(Object(external_usLibs_rating_["positivizeRating"])(result.Performance)));
            const rateElem = !result
                ? "-"
                : result.IsRated && contest.IsRated
                ? getRatingChangeElem(result.OldRating, result.NewRating)
                : getUnratedElem(result.OldRating);
            external_jQuery_(elem).append(
                `<td class="standings-result standings-perf">${perfElem}</td>`
            );
            external_jQuery_(elem).append(
                `<td class="standings-result standings-rate">${rateElem}</td>`
            );
            function getRatingChangeElem(oldRate, newRate) {
                return `<span class="bold">${getRatingSpan(
                    oldRate
                )}</span> → <span class="bold">${getRatingSpan(
                    newRate
                )}</span> <span class="grey">(${
                    newRate >= oldRate ? "+" : ""
                }${newRate - oldRate})</span>`;
            }
            function getUnratedElem(rate) {
                return `<span class="bold">${getRatingSpan(
                    rate
                )}</span> <span class="grey">(unrated)</span>`;
            }
            function getRatingSpan(rate) {
                return `<span class="user-${Object(external_usLibs_rating_["getColor"])(rate)}">${rate}</span>`;
            }
        });
    }
}

// EXTERNAL MODULE: ./src/elements/estimator/dom.html
var estimator_dom = __webpack_require__(8);
var estimator_dom_default = /*#__PURE__*/__webpack_require__.n(estimator_dom);

// CONCATENATED MODULE: ./src/elements/estimator/model/EstimatorModel.js
class EstimatorModel {
    constructor(inputValue, perfHistory) {
        this.inputDesc = "";
        this.resultDesc = "";
        this.perfHistory = perfHistory;
        this.updateInput(inputValue);
    }

    updateInput(value) {
        this.inputValue = value;
        this.resultValue = this.calcResult(value);
    }

    toggle() {}

    /**
     * @param {Number} [input]
     * @return {Number}
     */
    calcResult(input) {
        return input;
    }
}

// CONCATENATED MODULE: ./src/elements/estimator/model/CalcRatingModel.js




class CalcRatingModel_CalcRatingModel extends EstimatorModel {
    constructor(inputValue, perfHistory) {
        super(inputValue, perfHistory);
        this.inputDesc = "パフォーマンス";
        this.resultDesc = "到達レーティング";
    }

    toggle() {
        return new CalcPerfModel_CalcPerfModel(this.resultValue, this.perfHistory);
    }
    calcResult(input) {
        return Object(external_usLibs_rating_["positivizeRating"])(
            Object(external_usLibs_rating_["calcRatingFromHistory"])([input].concat(this.perfHistory))
        );
    }
}

// CONCATENATED MODULE: ./src/elements/estimator/model/CalcPerfModel.js




class CalcPerfModel_CalcPerfModel extends EstimatorModel {
    constructor(inputValue, perfHistory) {
        super(inputValue, perfHistory);
        this.inputDesc = "目標レーティング";
        this.resultDesc = "必要パフォーマンス";
    }

    toggle() {
        return new CalcRatingModel_CalcRatingModel(this.resultValue, this.perfHistory);
    }
    calcResult(input) {
        return Object(external_usLibs_rating_["calcRequiredPerformance"])(
            Object(external_usLibs_rating_["unpositivizeRating"])(input),
            this.perfHistory
        );
    }
}

// CONCATENATED MODULE: ./src/libs/utils/twitter.js
/**
 *
 * @param {string} [content]
 * @param {string} [url]
 * @return {string}
 */
function GetEmbedTweetLink(content, url) {
    return `https://twitter.com/share?text=${encodeURI(
        content
    )}&url=${encodeURI(url)}`;
}

// CONCATENATED MODULE: ./src/elements/estimator/script.js










let estimator = new external_sidemenu_["SideMenuElement"](
    "estimator",
    "Estimator",
    /atcoder.jp/,
    estimator_dom_default.a,
    script_afterAppend
);

async function script_afterAppend() {
    const estimatorInputSelector = external_jQuery_("#estimator-input");
    const estimatorResultSelector = external_jQuery_("#estimator-res");
    let model = GetModelFromStateCode(
        Object(external_usLibs_global_["getLS"])("sidemenu_estimator_state"),
        Object(external_usLibs_global_["getLS"])("sidemenu_estimator_value"),
        Object(external_usLibs_data_["getPerformanceHistories"])(await Object(external_usLibs_data_["getMyHistoryData"])())
    );
    updateView();

    external_jQuery_("#estimator-toggle").click(function() {
        model = model.toggle();
        updateLocalStorage();
        updateView();
    });
    estimatorInputSelector.keyup(() => {
        updateModel();
        updateLocalStorage();
        updateView();
    });

    /** modelをinputの値に応じて更新 */
    function updateModel() {
        const inputString = estimatorInputSelector.val();
        if (!isFinite(inputString)) return;
        const inputNumber = parseInt(inputString);
        model.updateInput(inputNumber);
    }

    /** modelの状態をLSに保存 */
    function updateLocalStorage() {
        Object(external_usLibs_global_["setLS"])("sidemenu_estimator_value", model.inputValue);
        Object(external_usLibs_global_["setLS"])("sidemenu_estimator_state", model.constructor.name);
    }

    /** modelを元にviewを更新 */
    function updateView() {
        const roundedInput = roundValue(model.inputValue, 2);
        const roundedResult = roundValue(model.resultValue, 2);

        external_jQuery_("#estimator-input-desc").text(model.inputDesc);
        external_jQuery_("#estimator-res-desc").text(model.resultDesc);
        estimatorInputSelector.val(roundedInput);
        estimatorResultSelector.val(roundedResult);

        const tweetStr = `AtCoderのハンドルネーム: ${external_usLibs_global_["userScreenName"]}\n${model.inputDesc}: ${roundedInput}\n${model.resultDesc}: ${roundedResult}\n`;
        external_jQuery_("#estimator-tweet").attr(
            "href",
            GetEmbedTweetLink(
                tweetStr,
                "https://greasyfork.org/ja/scripts/369954-ac-predictor"
            )
        );
    }
}

const models = [CalcPerfModel_CalcPerfModel, CalcRatingModel_CalcRatingModel];

/**
 * LocalStorageに保存されたステートコードから状態を復元します
 * @param {string} [state] ステートを示す文字列(型名)
 * @param {number} [value] 最初に入る値
 * @param {number[]} [history] パフォーマンス履歴(時間降順)
 * @return {EstimatorModel} 構築されたモデル
 */
function GetModelFromStateCode(state, value, history) {
    let model = models.find(model => model.name === state);
    if (!model) model = CalcPerfModel_CalcPerfModel;
    return new model(value, history);
}

// CONCATENATED MODULE: ./src/main.js
// ==UserScript==
// @name        ac-predictor
// @namespace   http://ac-predictor.azurewebsites.net/
// @version     1.2.6
// @description コンテスト中にAtCoderのパフォーマンスを予測します
// @author      keymoon
// @license     MIT
// @require     https://greasyfork.org/scripts/386715-atcoder-sidemenu/code/atcoder-sidemenu.js
// @require     https://greasyfork.org/scripts/386712-atcoder-userscript-libs/code/atcoder-userscript-libs.js
// @supportURL  https://github.com/key-moon/ac-predictor.user.js/issues
// @match       https://atcoder.jp/*
// @exclude     https://atcoder.jp/*/json
// ==/UserScript==





external_sidemenu_["sidemenu"].addElement(predictor);
external_sidemenu_["sidemenu"].addElement(estimator);


/***/ })
/******/ ]);