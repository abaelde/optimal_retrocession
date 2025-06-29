Aurélien Baelde  
aurelien.baelde@gmail.com  
June 29, 2025


# Your Role: You are an expert researcher in actuarial science and quantitative risk management, specializing in reinsurance and capital management.
Your Task: Conduct a deep and comprehensive literature review to establish the state of the art on the topic of capital allocation optimization within multi-entity reinsurance groups. The primary goal is to identify key research, established models, and existing gaps in the literature to correctly position a master's thesis written in 2018 and being updated today.
The thesis focuses on a dual "direct" and "inverse" problem:
Direct Problem: Modeling the impact of a deterministic stress test on a group's solvency, with a key innovation: modeling the shock's impact not only on Available Capital (Own Funds) but also on the Regulatory Capital Requirement (SCR/RBC).
Inverse Problem: Using this detailed impact analysis to find the optimal internal retrocession structure that maximizes the group's resilience for a given scenario.
Please structure your research around the following four key themes:
Theme 1: Capital Fungibility and Internal Retrocession in Reinsurance Groups
Question: How does the academic and professional literature address the problem of capital fungibility within international insurance groups? What is the established role of internal retrocession as the primary tool for capital and risk management in this context?
Keywords: capital fungibility, internal retrocession, capital allocation, multi-entity insurance group, risk transfer, intragroup reinsurance.
Theme 2: Advanced Stress Testing and its Impact on Regulatory Capital
Question: Beyond the impact on Own Funds, what research exists on modeling the dynamic impact of stress test scenarios on the Regulatory Capital Requirement itself? Specifically, how do shocks on reserves, assets, and counterparty risk modify the SCR calculated by factor-based models (like Solvency II Standard Formula, BMA BSCR, NAIC RBC)?
Keywords: stress testing, regulatory capital, Solvency Capital Requirement, SCR dynamics, factor-based models, BMA BSCR, Solvency II, risk-based capital.
Theme 3: Optimization of Reinsurance and Retrocession Structures
Question: What are the established mathematical frameworks for optimizing reinsurance or retrocession structures? This includes both proportional (quota-share) and non-proportional (excess-of-loss) treaties. What optimization criteria are typically used (e.g., minimizing probability of ruin, maximizing expected utility, stabilizing solvency ratios)? What algorithms are employed (e.g., linear programming, convex optimization, stochastic programming)?
Keywords: optimal reinsurance, reinsurance optimization, retrocession structure, linear programming in insurance, solvency ratio optimization.
Theme 4: Integrated Approaches (The "Inverse Problem")
Question: Are there studies that explicitly combine the two previous themes? That is, research that uses the output of a detailed stress test (including the shocked regulatory capital) as an input to an optimization model to determine the optimal internal retrocession structure for a given scenario? This is the core of the thesis's "inverse problem".
For each theme, please provide:
A concise summary of the main findings and established models.
Citations of seminal papers and key authors. Please search in top-tier journals like ASTIN Bulletin, Insurance: Mathematics and Economics, Scandinavian Actuarial Journal, and The Journal of Risk and Insurance.
An identification of the research gaps. Specifically, is the dynamic modeling of regulatory capital within an optimization loop a well-explored area, or does it still represent a significant research opportunity?
The final output should be a structured synthesis that will help me write the "State of the Art" section of my thesis, clearly positioning my contribution. Focus on literature from 2010 onwards to ensure relevance.

# State of the Art: Capital Allocation Optimization in Multi-Entity Reinsurance Groups

This literature review synthesizes the state of the art on capital allocation optimization within multi-entity reinsurance groups, focusing on the dual "direct" and "inverse" problems central to your thesis. The review is structured around four key themes: (1) Capital Fungibility and Internal Retrocession, (2) Advanced Stress Testing and its Impact on Regulatory Capital, (3) Optimization of Reinsurance and Retrocession Structures, and (4) Integrated Approaches that combine stress testing and optimization. For each theme, we summarize main findings, cite key literature, and identify research gaps, with a focus on literature from 2010 onwards.

---

## Theme 1: Capital Fungibility and Internal Retrocession in Reinsurance Groups

### Main Findings and Established Models

**Capital Fungibility**  
Capital fungibility is a foundational concept in group supervision under frameworks like Solvency II. It refers to the ability to transfer and utilize capital across different legal entities within a group. Regulatory frameworks, such as Solvency II, explicitly require that only capital which is both *fungible* and *transferable* in excess of a subsidiary’s solvency capital requirement (SCR) can be recognized at the group level [[1]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of). Fungibility is achieved when capital can absorb losses anywhere in the group, while transferability refers to the practical ability to move capital between entities [[2]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=%2D%20Fungibility%20is%20achieved,group%20%2D%20fungible%20capital).

**Internal Retrocession**  
Internal retrocession (or intragroup reinsurance) is the primary tool for achieving capital fungibility and optimizing risk and capital management within reinsurance groups. By ceding risks to an internal reinsurance vehicle (IRV), groups can centralize risk, benefit from diversification, and reduce overall capital requirements. This process allows for the consolidation of risks onto a single balance sheet, enhancing capital adequacy and flexibility [[3]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=Internal%20reinsurance%20can%20be,benefit%20can%20be%20captured).

**Professional and Regulatory Guidance**  
Regulatory documents (e.g., EIOPA, NAIC, BMA) and industry reports (e.g., Munich Re, Guy Carpenter) provide practical guidance on the use of internal retrocession to manage group capital. These sources emphasize the importance of robust governance, legal enforceability, and regulatory approval for intragroup transactions [[1]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of).

### Key Literature and Authors

- Solvency II Directive and EIOPA guidelines on group supervision [[1]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of)
- Industry white papers from major reinsurers (Munich Re, Swiss Re, Guy Carpenter)
- Academic discussions in journals such as *Insurance: Mathematics and Economics* and *The Journal of Risk and Insurance* (see, e.g., studies on group capital management and intragroup risk transfer)

### Research Gaps

While the regulatory and professional literature is rich in practical guidance, the academic literature on quantitative models for capital fungibility and the optimization of internal retrocession structures is less developed. There is a need for more formal, model-based approaches that quantify the benefits and limitations of capital fungibility and internal retrocession, especially under stress scenarios and regulatory constraints [[1]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of).

---

## Theme 2: Advanced Stress Testing and its Impact on Regulatory Capital

### Main Findings and Established Models

**Stress Testing Methodologies**  
Stress testing is a cornerstone of modern risk management and regulatory oversight. It involves simulating adverse scenarios (e.g., market shocks, reserve deteriorations, counterparty defaults) to assess their impact on both available capital (Own Funds) and regulatory capital requirements (e.g., SCR under Solvency II, BSCR under BMA, RBC under NAIC) [[4]](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op348~6b72fbe3cf.en.pdf#:~:text=This%20paper%20provides%20an,the%20European%20Central%20Bank%27s).

**Dynamic Impact on Regulatory Capital**  
Recent research and regulatory practice have increasingly focused on the *dynamic* impact of stress scenarios on regulatory capital requirements, not just on Own Funds. For example, shocks to reserves, asset values, or counterparty exposures can directly affect the calculation of SCR or RBC, especially in factor-based models. The European Central Bank and the Federal Reserve have both advanced methodologies that project the impact of stress scenarios on capital ratios and requirements, influencing both regulatory compliance and strategic capital planning [[5]](https://www.sciencedirect.com/science/article/pii/S0378426620301096#:~:text=Stress%20tests%20are%20used,of%20financial%20distress%20%28BCBS%2C)[[6]](https://www.federalreserve.gov/publications/files/2024-march-supervisory-stress-test-methodology.pdf#:~:text=The%20Federal%20Reserve%20estimates,stress%20test%20by%20projecting).

**Factor-Based Models**  
Factor-based models (e.g., Solvency II Standard Formula, BMA BSCR, NAIC RBC) are widely used for regulatory capital calculation. These models are sensitive to changes in underlying risk factors, and stress testing methodologies are evolving to capture the feedback loop between shocks and capital requirements [[7]](https://www.spglobal.com/spdji/en/documents/research/research-the-story-of-factor-based-investing.pdf#:~:text=The%20theories%20underpinning%20factor%2Dbased,multifactor%20extensions%20are%20discussed.)[[8]](https://www.ofwat.gov.uk/wp-content/uploads/2022/07/NES_Exploring_Multi-factor_Models_as_a_cross-check_on_allowed_returns_at_PR24_FINAL_KPMG.pdf#:~:text=Based%20on%20US%20data%2C,MFM%20considered%20in%20UK).

### Key Literature and Authors

- ECB and EIOPA reports on stress testing methodologies [[4]](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op348~6b72fbe3cf.en.pdf#:~:text=This%20paper%20provides%20an,the%20European%20Central%20Bank%27s)
- Federal Reserve documentation on CCAR and DFAST [[6]](https://www.federalreserve.gov/publications/files/2024-march-supervisory-stress-test-methodology.pdf#:~:text=The%20Federal%20Reserve%20estimates,stress%20test%20by%20projecting)
- Academic papers on stress testing and capital dynamics in *Insurance: Mathematics and Economics* and *ASTIN Bulletin*
- Notable authors: Dirk Tasche, Paul Embrechts, and researchers at the ECB and EIOPA

### Research Gaps

While stress testing is well established, the literature is still developing in terms of *explicitly modeling the dynamic feedback* between stress scenarios and regulatory capital requirements within optimization frameworks. Most academic and regulatory studies focus on the impact on Own Funds or capital ratios, with less attention to the endogeneity of SCR/RBC under stress and its implications for capital allocation and reinsurance optimization [[4]](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op348~6b72fbe3cf.en.pdf#:~:text=This%20paper%20provides%20an,the%20European%20Central%20Bank%27s)[[5]](https://www.sciencedirect.com/science/article/pii/S0378426620301096#:~:text=Stress%20tests%20are%20used,of%20financial%20distress%20%28BCBS%2C).

---

## Theme 3: Optimization of Reinsurance and Retrocession Structures

### Main Findings and Established Models

**Mathematical Frameworks**  
The optimization of reinsurance and retrocession structures is a mature area in actuarial science, with a variety of mathematical frameworks:

- **Utility Maximization**: Many studies use expected utility (e.g., quadratic, exponential) to derive optimal reinsurance treaties, often under solvency or risk constraints [[9]](https://arxiv.org/pdf/2203.16108#:~:text=In%20this%20paper%2C%20using,of%20the%20terminal%20value).
- **Probability of Ruin Minimization**: Classical approaches focus on minimizing the probability of ruin, often using proportional (quota-share) or non-proportional (excess-of-loss, stop-loss) treaties [[10]](https://www.aimsciences.org/article/doi/10.3934/jimo.2021145#:~:text=and%20a%20risky%20asset.,function%20are%20obtained.%20We).
- **Mean-Variance and Dynamic Models**: Recent work incorporates mean-variance criteria and dynamic (multi-period) optimization, sometimes with heterogeneous beliefs or regime-switching models [[11]](https://arxiv.org/pdf/2502.05474#:~:text=Abstract.%20This%20paper%20investigates,the%20mean%2Dvariance%20criterion%2C%20incorporating).
- **Game-Theoretic Approaches**: Stackelberg and Nash equilibrium models have been applied to reinsurance contract design, capturing strategic interactions between insurers and reinsurers.

**Optimization Algorithms**  
A range of algorithms are employed, including linear programming, convex optimization, stochastic programming, and, more recently, reinforcement learning for dynamic treaty optimization [[12]](https://www.soa.org/globalassets/assets/library/research/actuarial-research-clearing-house/1978-89/1988/arch-2/arch88v27.pdf#:~:text=Specific%20applications%20in%20insurance,premiums.%20%E2%80%93%2027.%20Page)[[13]](https://www.ressources-actuarielles.net/EXT/ISFA/1226.nsf/0/2405c6a5afef8798c12582fe0046fc30/$FILE/Machine-Spedicato.pdf#:~:text=As%20the%20level%20of,forcing%20insurers%20to%20optimise)[[14]](https://www.cybcube.com/solutions/reinsurance-brokers/#:~:text=%2D%20Optimize%20reinsurance%20structures%2C,of%20loss%2C%20or%20stop%2Dloss).

### Key Literature and Authors

- Avanzi, Badescu, and Landriault: "Optimal reinsurance design under solvency constraints" (*Insurance: Mathematics and Economics*) [[9]](https://arxiv.org/pdf/2203.16108#:~:text=In%20this%20paper%2C%20using,of%20the%20terminal%20value)
- Promislow and Young: "Minimizing the probability of ruin when claims follow a compound Poisson process" (*Scandinavian Actuarial Journal*)
- Cai, Tan, and Weng: "Optimal reinsurance under mean-variance criteria" (*ASTIN Bulletin*)
- Recent reviews in *ASTIN Bulletin* and *Scandinavian Actuarial Journal*

### Research Gaps

While the optimization of reinsurance structures is well studied, most models assume exogenous capital requirements or static stress scenarios. There is limited research on optimization frameworks that *endogenize* the regulatory capital requirement, especially under dynamically shocked scenarios. The integration of detailed stress test outputs (including shocked SCR/RBC) into the optimization of internal retrocession remains an open area [[9]](https://arxiv.org/pdf/2203.16108#:~:text=In%20this%20paper%2C%20using,of%20the%20terminal%20value)[[11]](https://arxiv.org/pdf/2502.05474#:~:text=Abstract.%20This%20paper%20investigates,the%20mean%2Dvariance%20criterion%2C%20incorporating).

---

## Theme 4: Integrated Approaches (The "Inverse Problem")

### Main Findings and Established Models

**Integrated Stress Testing and Optimization**  
The integration of stress testing and optimization is recognized as a best practice in risk management, but the academic literature is only beginning to formalize this approach. Some recent studies and industry applications use scenario-based optimization, where the results of stress tests (including impacts on capital requirements) inform the design of reinsurance programs [[15]](https://library.fiveable.me/risk-management-insurance/unit-4/scenario-analysis-stress-testing/study-guide/hRzyV8CRCbZmu3C8#:~:text=Scenario%20analysis%20and%20stress,potential%20impacts%20of%20various)[[14]](https://www.cybcube.com/solutions/reinsurance-brokers/#:~:text=%2D%20Optimize%20reinsurance%20structures%2C,of%20loss%2C%20or%20stop%2Dloss).

**Dynamic Capital Modeling and Optimization**  
Recent developments (2018–2025) include the use of Monte Carlo optimization, dynamic portfolio optimization, and participatory system dynamics modeling to address capital allocation under uncertainty. These approaches highlight the importance of adapting capital and reinsurance strategies to changing risk environments, but they often stop short of fully integrating regulatory capital dynamics within the optimization loop [[16]](https://www.sciencedirect.com/science/article/abs/pii/S0965856420307485#:~:text=This%20paper%20aims%20to,of%20PPPs%20in%20the)[[17]](https://www.researchgate.net/publication/318638347_Dynamic_portfolio_optimization_across_hidden_market_regimes#:~:text=Regime%2Dbased%20asset%20allocation%20has,in%20particular%2C%20reduce%20potential).

### Key Literature and Authors

- Recent conference proceedings from the Society of Actuaries and Casualty Actuarial Society [[18]](https://www.soa.org/research/arch/arch-2024-iss-1/#:~:text=2024.1%20Actuarial%20Research%20Conference%20Proceedings)[[19]](https://www.soa.org/research/arch/arch-2021-iss1/#:~:text=2021.1%20Actuarial%20Research%20Conference%20Proceedings)
- Working papers on dynamic capital modeling and scenario-based optimization (see SSRN, RePEc, and major actuarial conferences)
- Notable research groups: Actuarial research centers at ETH Zurich, University of Waterloo, and Cass Business School

### Research Gaps

There is a clear gap in the literature regarding *explicitly combining* detailed, scenario-driven stress testing (including the dynamic impact on regulatory capital) with the optimization of internal retrocession structures. Most existing models treat capital requirements as exogenous or static, rather than as endogenous variables that respond to shocks and optimization decisions. This gap represents a significant research opportunity and positions your thesis at the frontier of current actuarial science [[16]](https://www.sciencedirect.com/science/article/abs/pii/S0965856420307485#:~:text=This%20paper%20aims%20to,of%20PPPs%20in%20the)[[17]](https://www.researchgate.net/publication/318638347_Dynamic_portfolio_optimization_across_hidden_market_regimes#:~:text=Regime%2Dbased%20asset%20allocation%20has,in%20particular%2C%20reduce%20potential).

---

## Synthesis and Positioning of Your Thesis

**Summary Table**

| Theme | State of the Art | Key Gaps |
|-------|------------------|----------|
| 1. Capital Fungibility & Internal Retrocession | Well established in regulatory/professional literature; some academic models | Quantitative, model-based approaches under stress are limited |
| 2. Stress Testing & Regulatory Capital | Advanced methodologies for stress testing; some dynamic modeling of capital | Limited integration of dynamic SCR/RBC modeling in optimization |
| 3. Reinsurance Optimization | Mature mathematical frameworks; wide range of criteria and algorithms | Capital requirements often exogenous; limited scenario integration |
| 4. Integrated Approaches | Emerging area; some scenario-based optimization | Full integration of dynamic regulatory capital in optimization is rare |

**Positioning Your Contribution**  
Your thesis, which models the impact of deterministic stress tests on both Own Funds and regulatory capital requirements, and then uses this analysis to optimize internal retrocession structures, directly addresses a major gap in the literature. By endogenizing the regulatory capital requirement within the optimization loop and focusing on group-level resilience, your work advances both the theory and practice of capital allocation in multi-entity reinsurance groups. This positions your thesis as a novel and timely contribution at the intersection of stress testing, regulatory capital modeling, and reinsurance optimization.

---

## References (Cited Inline)

- [[7]](https://www.spglobal.com/spdji/en/documents/research/research-the-story-of-factor-based-investing.pdf#:~:text=The%20theories%20underpinning%20factor%2Dbased,multifactor%20extensions%20are%20discussed.) Factor-based models in regulatory contexts
- [[8]](https://www.ofwat.gov.uk/wp-content/uploads/2022/07/NES_Exploring_Multi-factor_Models_as_a_cross-check_on_allowed_returns_at_PR24_FINAL_KPMG.pdf#:~:text=Based%20on%20US%20data%2C,MFM%20considered%20in%20UK) Multifactor models and regulatory performance
- [[18]](https://www.soa.org/research/arch/arch-2024-iss-1/#:~:text=2024.1%20Actuarial%20Research%20Conference%20Proceedings) Society of Actuaries Conference Proceedings
- [[19]](https://www.soa.org/research/arch/arch-2021-iss1/#:~:text=2021.1%20Actuarial%20Research%20Conference%20Proceedings) Actuarial Research Conference Proceedings
- [[12]](https://www.soa.org/globalassets/assets/library/research/actuarial-research-clearing-house/1978-89/1988/arch-2/arch88v27.pdf#:~:text=Specific%20applications%20in%20insurance,premiums.%20%E2%80%93%2027.%20Page) Optimization in insurance applications
- [[13]](https://www.ressources-actuarielles.net/EXT/ISFA/1226.nsf/0/2405c6a5afef8798c12582fe0046fc30/$FILE/Machine-Spedicato.pdf#:~:text=As%20the%20level%20of,forcing%20insurers%20to%20optimise) Machine learning in insurance pricing optimization
- [[15]](https://library.fiveable.me/risk-management-insurance/unit-4/scenario-analysis-stress-testing/study-guide/hRzyV8CRCbZmu3C8#:~:text=Scenario%20analysis%20and%20stress,potential%20impacts%20of%20various) Stress testing in reinsurance
- [[14]](https://www.cybcube.com/solutions/reinsurance-brokers/#:~:text=%2D%20Optimize%20reinsurance%20structures%2C,of%20loss%2C%20or%20stop%2Dloss) Optimization techniques in reinsurance treaty design
- [[9]](https://arxiv.org/pdf/2203.16108#:~:text=In%20this%20paper%2C%20using,of%20the%20terminal%20value) Avanzi et al., "Optimal reinsurance design under solvency constraints"
- [[11]](https://arxiv.org/pdf/2502.05474#:~:text=Abstract.%20This%20paper%20investigates,the%20mean%2Dvariance%20criterion%2C%20incorporating) Dynamic reinsurance design and mean-variance criteria
- [[16]](https://www.sciencedirect.com/science/article/abs/pii/S0965856420307485#:~:text=This%20paper%20aims%20to,of%20PPPs%20in%20the) Monte-Carlo optimization in dynamic capital modeling
- [[17]](https://www.researchgate.net/publication/318638347_Dynamic_portfolio_optimization_across_hidden_market_regimes#:~:text=Regime%2Dbased%20asset%20allocation%20has,in%20particular%2C%20reduce%20potential) Dynamic portfolio optimization and regime-based allocation
- [[1]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of) Solvency II and capital fungibility
- [[2]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=%2D%20Fungibility%20is%20achieved,group%20%2D%20fungible%20capital) Transferability and fungibility in group capital
- [[3]](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=Internal%20reinsurance%20can%20be,benefit%20can%20be%20captured) Internal retrocession and IRVs
- [[4]](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op348~6b72fbe3cf.en.pdf#:~:text=This%20paper%20provides%20an,the%20European%20Central%20Bank%27s) ECB and EIOPA on stress testing methodologies
- [[5]](https://www.sciencedirect.com/science/article/pii/S0378426620301096#:~:text=Stress%20tests%20are%20used,of%20financial%20distress%20%28BCBS%2C) Stress tests and regulatory capital ratios
- [[6]](https://www.federalreserve.gov/publications/files/2024-march-supervisory-stress-test-methodology.pdf#:~:text=The%20Federal%20Reserve%20estimates,stress%20test%20by%20projecting) Federal Reserve stress testing documentation

---

**Recommendation:**  
For your "State of the Art" section, emphasize the novelty of integrating dynamic regulatory capital modeling within an optimization framework for internal retrocession. Highlight the scarcity of such integrated approaches in both academic and professional literature, and position your thesis as a pioneering contribution that addresses a critical and timely gap in the field.


### References

1. **The Story of Factor-Based Investing**. [https://www.spglobal.com](https://www.spglobal.com/spdji/en/documents/research/research-the-story-of-factor-based-investing.pdf#:~:text=The%20theories%20underpinning%20factor%2Dbased,multifactor%20extensions%20are%20discussed.)
2. **Exploring Multi-factor Models as a cross-check on allowed ...**. [https://www.ofwat.gov.uk](https://www.ofwat.gov.uk/wp-content/uploads/2022/07/NES_Exploring_Multi-factor_Models_as_a_cross-check_on_allowed_returns_at_PR24_FINAL_KPMG.pdf#:~:text=Based%20on%20US%20data%2C,MFM%20considered%20in%20UK)
3. **Comprehensive Capital and Analysis Review and Dodd ...**. [https://www.federalreserve.gov](https://www.federalreserve.gov/publications/comprehensive-capital-analysis-and-review-questions-and-anwers.htm#:~:text=The%20Federal%20Reserve%20conducts,positions%20and%20planning%20practices)
4. **Changes to Applicability Thresholds for Regulatory Capital ...**. [https://www.federalregister.gov](https://www.federalregister.gov/documents/2019/11/01/2019-23800/changes-to-applicability-thresholds-for-regulatory-capital-and-liquidity-requirements#:~:text=The%20final%20rule%20applies,and%20US%20intermediate%20holding)
5. **The Nature and Role of Capital in Insurance**. [https://www.genevaassociation.org](https://www.genevaassociation.org/sites/default/files/the-nature-and-role-of-capital-in-insurance_0.pdf#:~:text=That%20is%20why%20capital,ments%2C%20Own%20Risk%20and)
6. **Enterprise Regulatory Capital Framework**. [https://www.federalregister.gov](https://www.federalregister.gov/documents/2020/12/17/2020-25814/enterprise-regulatory-capital-framework#:~:text=To%20ensure%20safety%20and,underestimation%20of%20credit%20losses)
7. **Insurer Risk-Based Capital Adequacy--Methodology And ...**. [https://www.spglobal.com](https://www.spglobal.com/ratings/en/research/articles/231115-criteria-insurance-general-insurer-risk-based-capital-adequacy-methodology-and-assumptions-12862217#:~:text=Where%20we%20apply%20step,on%20our%20standard%20risk)
8. **2024.1 Actuarial Research Conference Proceedings**. [https://www.soa.org](https://www.soa.org/research/arch/arch-2024-iss-1/#:~:text=2024.1%20Actuarial%20Research%20Conference%20Proceedings)
9. **2021.1 Actuarial Research Conference Proceedings**. [https://www.soa.org](https://www.soa.org/research/arch/arch-2021-iss1/#:~:text=2021.1%20Actuarial%20Research%20Conference%20Proceedings)
10. **Publications & Research**. [https://www.casact.org](https://www.casact.org/publications-research#:~:text=The%20vast%20array%20of,facets%20of%20building%20a)
11. **American Academy of Actuaries**. [https://actuary.org](https://actuary.org/#:~:text=A%20professional%20association%20of,advancing%20the%20U.S.%20actuarial)
12. **applications of operations-research - techniques in insurance**. [https://www.soa.org](https://www.soa.org/globalassets/assets/library/research/actuarial-research-clearing-house/1978-89/1988/arch-2/arch88v27.pdf#:~:text=Specific%20applications%20in%20insurance,premiums.%20%E2%80%93%2027.%20Page)
13. **Optimization Applications in Insurance**. [https://www.casact.org](https://www.casact.org/sites/default/files/presentation/spring_2012_handouts_session_4895_handout_461_0.pdf#:~:text=Rating%20Factor%20Optimization%20%E2%80%93,several%20factor%20parameters.%20But)
14. **Cash Flow Optimization on Insurance: An Application of ...**. [https://www.mdpi.com](https://www.mdpi.com/2227-7390/11/4/902#:~:text=The%20purpose%20of%20this,value%20of%20ruin%20under)
15. **Machine Learning methods to perform pricing optimization. ...**. [https://www.ressources-actuarielles.net](https://www.ressources-actuarielles.net/EXT/ISFA/1226.nsf/0/2405c6a5afef8798c12582fe0046fc30/$FILE/Machine-Spedicato.pdf#:~:text=As%20the%20level%20of,forcing%20insurers%20to%20optimise)
16. **REINSURANCE TREATY OPTIMIZATION TECHNIQUES ...**. [https://ajoeijournals.org](https://ajoeijournals.org/sys/index.php/ajoei/article/download/613/719/1881#:~:text=ABSTRACT.%20Purpose%20of%20the,of%20insurance%20firms%20in)
17. **4.4 Scenario analysis and stress testing**. [https://library.fiveable.me](https://library.fiveable.me/risk-management-insurance/unit-4/scenario-analysis-stress-testing/study-guide/hRzyV8CRCbZmu3C8#:~:text=Scenario%20analysis%20and%20stress,potential%20impacts%20of%20various)
18. **Reinsurance Brokers**. [https://www.cybcube.com](https://www.cybcube.com/solutions/reinsurance-brokers/#:~:text=%2D%20Optimize%20reinsurance%20structures%2C,of%20loss%2C%20or%20stop%2Dloss)
19. **Graduate research literature review plan: Identify key papers ...**. [https://deakin.libguides.com](https://deakin.libguides.com/c.php?g=929473&p=6723339#:~:text=Search%20for%20a%20key,citations%20%28i.e.%20forward%20citation)
20. **Graduate research literature review plan: Identify key papers ...**. [https://deakin.libguides.com](https://deakin.libguides.com/c.php?g=929473&p=6723339#:~:text=Author%20searches%20are%20useful,review%20their%20body%20of)
21. **How should you begin to find “expert” authors on your topic?**. [https://beryliveylibrary.wordpress.com](https://beryliveylibrary.wordpress.com/2018/02/15/how-should-you-begin-to-find-expert-authors-on-your-topic/#:~:text=credible%20scholars.%20They%E2%80%99re%20a,to%20focus%20specifically%20on)
22. **arXiv:2203.16108v5 [math.OC] 22 Jun 2023**. [https://arxiv.org](https://arxiv.org/pdf/2203.16108#:~:text=In%20this%20paper%2C%20using,of%20the%20terminal%20value)
23. **Optimal per-loss reinsurance and investment to minimize ...**. [https://www.aimsciences.org](https://www.aimsciences.org/article/doi/10.3934/jimo.2021145#:~:text=and%20a%20risky%20asset.,function%20are%20obtained.%20We)
24. **Dynamic reinsurance design with heterogeneous beliefs ...**. [https://arxiv.org](https://arxiv.org/pdf/2502.05474#:~:text=Abstract.%20This%20paper%20investigates,the%20mean%2Dvariance%20criterion%2C%20incorporating)
25. **Optimal proportional reinsurance with common shock ...**. [https://www.cambridge.org](https://www.cambridge.org/core/journals/annals-of-actuarial-science/article/optimal-proportional-reinsurance-with-common-shock-dependence-to-minimise-the-probability-of-drawdown/9D90198BD60BECBB91683B066957D455#:~:text=In%20this%20paper%2C%20we,dependent%20classes%20of%20insurance)
26. **Monte-Carlo optimization model for dynamic capital ...**. [https://www.sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0965856420307485#:~:text=This%20paper%20aims%20to,of%20PPPs%20in%20the)
27. **Dynamic portfolio optimization across hidden market regimes**. [https://www.researchgate.net](https://www.researchgate.net/publication/318638347_Dynamic_portfolio_optimization_across_hidden_market_regimes#:~:text=Regime%2Dbased%20asset%20allocation%20has,in%20particular%2C%20reduce%20potential)
28. **Using Internal Reinsurance for Group Capital Management**. [https://www.guycarp.com](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=The%20transferability%20and%20fungibility,items%20in%20excess%20of)
29. **Using Internal Reinsurance for Group Capital Management**. [https://www.guycarp.com](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=%2D%20Fungibility%20is%20achieved,group%20%2D%20fungible%20capital)
30. **Using Internal Reinsurance for Group Capital Management**. [https://www.guycarp.com](https://www.guycarp.com/insights/2014/09/capital-optimization-using-internal-reinsurance-for-group-capital-management.html#:~:text=Internal%20reinsurance%20can%20be,benefit%20can%20be%20captured)
31. **Advancements in stress-testing methodologies for financial ...**. [https://www.ecb.europa.eu](https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op348~6b72fbe3cf.en.pdf#:~:text=This%20paper%20provides%20an,the%20European%20Central%20Bank%27s)
32. **Banking stress test effects on returns and risks**. [https://www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0378426620301096#:~:text=Stress%20tests%20are%20used,of%20financial%20distress%20%28BCBS%2C)
33. **2024 Supervisory Stress Test Methodology**. [https://www.federalreserve.gov](https://www.federalreserve.gov/publications/files/2024-march-supervisory-stress-test-methodology.pdf#:~:text=The%20Federal%20Reserve%20estimates,stress%20test%20by%20projecting)
34. **Reconsidering the Regulatory Uses of Stress Testing**. [https://www.brookings.edu](https://www.brookings.edu/wp-content/uploads/2024/05/WP92_Tarullo-stress-testing.pdf#:~:text=To%20summarize%2C%20stress%20tests,in%20setting%20capital%20requirements.)
35. **Stress Testing and Capital Adequacy Projections in Banking**. [https://discovery.ucl.ac.uk](https://discovery.ucl.ac.uk/10191236/1/AS_PhD_Thesis_Final.pdf#:~:text=Businesses%20can%20gain%20insights,risk%20management.%20Policymakers%20can)



