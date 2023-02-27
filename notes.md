# Search Problem

## Definitions

**State Space:**
    Set of possible states.

**Initial State:**
    The state the agent starts in.

**Goal State:**
    Any state that satisfies the end goal.

**Goal Test:**
    Determines whether a state is a goal state.

**Actions:**
    Things that can be done in a given state.

**Transition Model:**
    The state resulting from an agent performing in action in a state.

**Action Cost Function:**
    Function that assigns a numeric cost to an action in a given state.

**Path:**
    Sequence of actions.

**Solution:**
    Path from the initial state to a goal state.

**Optimal Solution:**
    Solution with the lowest cost.

**Search Strategy:**
    How the next action is chosen.

---

State space can be represented as a **graph**:

- A node is a **state**.
- Connections between nodes are **actions**.

## Travelling Salesman Problem

A salesman needs to visit every city in an area with the least distance travelled.